"""Apply page layout to Quarto's DOCX output, without changing document content.

Quarto supplies only the output files of this render. No notebook, cache or
source file is opened. This helper uses Python's standard library only.
"""
from copy import deepcopy
from io import BytesIO
import os
from pathlib import Path
import re
import tempfile
import xml.etree.ElementTree as ET
from zipfile import ZipFile

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}


def serialize(root, original):
    # Keep OOXML namespace prefixes, including the names in mc:Ignorable.
    namespaces = dict(data for _, data in ET.iterparse(BytesIO(original), events=("start-ns",)))
    for prefix, uri in namespaces.items():
        ET.register_namespace(prefix, uri)
    result = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    declaration_end = result.find(b"?>") + 2
    root_end = result.find(b">", declaration_end)
    missing = []
    for prefix, uri in namespaces.items():
        name = f"xmlns:{prefix}" if prefix else "xmlns"
        if not re.search(rb"\s" + name.encode() + rb"=", result[declaration_end:root_end]):
            missing.append(f' {name}="{uri}"'.encode())
    return result[:root_end] + b"".join(missing) + result[root_end:]


def element(name, **attributes):
    node = ET.Element(f"{{{W}}}{name}")
    for key, value in attributes.items():
        node.set(f"{{{W}}}{key}", str(value))
    return node


def section(template, numbering, start=1, footer=True):
    node = deepcopy(template)
    for tag in ("pgNumType", "type", "titlePg"):
        for old in node.findall(f"w:{tag}", NS):
            node.remove(old)
    if not footer:
        # A first-page cover footer is intentionally empty.
        node.append(element("titlePg"))
    node.append(element("type", val="nextPage"))
    node.append(element("pgNumType", fmt=numbering, start=start))
    return node


def section_break(node):
    paragraph = element("p")
    properties = element("pPr")
    properties.append(node)
    paragraph.append(properties)
    return paragraph


def format_docx(path):
    with ZipFile(path) as archive:
        members = [(entry, archive.read(entry.filename)) for entry in archive.infolist()]
    contents = dict((entry.filename, data) for entry, data in members)
    root = ET.fromstring(contents["word/document.xml"])
    body = root.find("w:body", NS)
    template = body.find("w:sectPr", NS)
    if template is None:
        raise ValueError("Missing DOCX section layout")
    # Pandoc adds a footnote setting to the template's page layout.
    cover = next((node for node in body if node.find(".//w:pStyle[@w:val='TOCHeading']", NS) is not None), None)
    first = next((node for node in body if node.find("w:pPr/w:pStyle[@w:val='Heading1']", NS) is not None), None)
    if cover is None or first is None:
        raise ValueError("Missing contents or first chapter; refusing an uncertain layout")
    body.insert(list(body).index(cover), section_break(section(template, "decimal", footer=False)))
    body.insert(list(body).index(first), section_break(section(template, "lowerRoman")))
    body.remove(template)
    body.append(section(template, "decimal"))
    # Do not duplicate the first chapter's section break with a style page break.
    first.find("w:pPr", NS).append(element("pageBreakBefore", val="0"))
    for table in body.findall(".//w:tbl", NS):
        rows = table.findall("w:tr", NS)
        for row in rows:
            properties = row.find("w:trPr", NS)
            if properties is None:
                properties = element("trPr")
                row.insert(0, properties)
            if properties.find("w:cantSplit", NS) is None:
                properties.append(element("cantSplit"))
        # Repeat the actual Pandoc header, never promote a data row to a header.
        if rows and rows[0].find("w:trPr/w:tblHeader", NS) is not None:
            rows[0].find("w:trPr/w:tblHeader", NS).set(f"{{{W}}}val", "true")
    contents["word/document.xml"] = serialize(root, contents["word/document.xml"])
    settings = ET.fromstring(contents["word/settings.xml"])
    for tag in ("updateFields", "autoHyphenation"):
        node = settings.find(f"w:{tag}", NS)
        if node is None:
            node = element(tag)
            settings.append(node)
        node.set(f"{{{W}}}val", "true")
    compatibility = settings.find("w:compat", NS)
    if compatibility is None:
        compatibility = element("compat")
        settings.append(compatibility)
    if compatibility.find("w:doNotExpandShiftReturn", NS) is None:
        compatibility.append(element("doNotExpandShiftReturn"))
    contents["word/settings.xml"] = serialize(settings, contents["word/settings.xml"])
    # Atomic replacement beside the generated output. All other ZIP members,
    # including images, mathematical expressions and relationships, are copied.
    with tempfile.NamedTemporaryFile(dir=path.parent, suffix=".docx", delete=False) as temporary:
        target = Path(temporary.name)
    try:
        with ZipFile(target, "w") as archive:
            for entry, data in members:
                archive.writestr(entry, contents.get(entry.filename, data))
        target.replace(path)
    finally:
        if target.exists():
            target.unlink()
    print(f"DOCX page layout: {path.name}")


if __name__ == "__main__":
    project = Path(os.environ.get("QUARTO_PROJECT_DIR", ".")).resolve()
    output = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", project / "_book")).resolve()
    for filename in os.environ.get("QUARTO_PROJECT_OUTPUT_FILES", "").splitlines():
        path = (project / filename).resolve()
        if path.suffix.lower() == ".docx":
            if not path.is_relative_to(output):
                raise ValueError("DOCX output is outside the configured output directory")
            format_docx(path)
