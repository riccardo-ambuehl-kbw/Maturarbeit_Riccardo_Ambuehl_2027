"""Build the shared Word style template; requires existing python-docx and Quarto.

Run manually after changing this file. Notebook code is never executed here.
The checked-in reference.docx is used directly during normal Quarto renders.
"""
from io import BytesIO
from pathlib import Path
import subprocess

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


def build():
    template = subprocess.run(
        ["quarto", "pandoc", "--print-default-data-file", "reference.docx"],
        check=True, capture_output=True,
    ).stdout
    document = Document(BytesIO(template))
    for style in document.styles:
        if style.type == 1:  # paragraph styles
            style.font.name = "Times New Roman"
            style.font.size = Pt(11)
            style.font.color.rgb = RGBColor(0, 0, 0)
            style.paragraph_format.line_spacing = 1.2
            style.paragraph_format.widow_control = True
    for name in ("Normal", "Body Text", "First Paragraph", "Compact"):
        style = document.styles[name]
        style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        style.paragraph_format.space_before = Pt(0)
        style.paragraph_format.space_after = Pt(6 if name != "Compact" else 0)
    for level, size in enumerate((16, 13, 11.5, 11), 1):
        style = document.styles[f"Heading {level}"]
        style.font.size = Pt(size)
        style.font.bold = True
        style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        style.paragraph_format.keep_with_next = True
        style.paragraph_format.space_before = Pt(16 if level > 1 else 0)
        style.paragraph_format.space_after = Pt(6)
        style.paragraph_format.page_break_before = level == 1
    for name in ("Title", "Author", "Date"):
        style = document.styles[name]
        style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        style.font.color.rgb = RGBColor(0, 0, 0)
    document.styles["Title"].font.size = Pt(22)
    document.styles["Title"].paragraph_format.space_before = Cm(4)
    document.styles["TOC Heading"].font.size = Pt(16)
    document.styles["TOC Heading"].font.bold = True
    document.styles["TOC Heading"].paragraph_format.keep_with_next = True
    source = document.styles.add_style("Source Code", WD_STYLE_TYPE.PARAGRAPH)
    source.style_id = "SourceCode"
    source.base_style = document.styles["Normal"]
    source.font.name = "Consolas"
    source.font.size = Pt(9)
    source.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    source.paragraph_format.line_spacing = 1.0
    source.paragraph_format.space_before = Pt(4)
    source.paragraph_format.space_after = Pt(4)
    source.paragraph_format.keep_with_next = False
    shading = OxmlElement("w:shd")
    shading.set(qn("w:fill"), "F6F8FA")
    source.element.get_or_add_pPr().append(shading)
    wrap = source.element.get_or_add_pPr().find(qn("w:wordWrap"))
    if wrap is None:
        wrap = OxmlElement("w:wordWrap")
        source.element.get_or_add_pPr().append(wrap)
    wrap.set(qn("w:val"), "on")
    document.styles["Verbatim Char"].font.name = "Consolas"
    document.styles["Verbatim Char"].font.size = Pt(9)
    bibliography = document.styles["Bibliography"]
    bibliography.paragraph_format.left_indent = Cm(0.75)
    bibliography.paragraph_format.first_line_indent = Cm(-0.75)
    bibliography.paragraph_format.space_before = Pt(0)
    bibliography.paragraph_format.space_after = Pt(6)
    bibliography.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    for style in document.styles:
        if style.style_id in ("FootnoteText", "FootnoteReference"):
            style.font.size = Pt(9)
    # Explicit fonts must override Pandoc's inherited Office theme fonts.
    for style in list(document.styles):
        if style.type == WD_STYLE_TYPE.PARAGRAPH:
            linked = style.element.find(qn("w:link"))
            if linked is not None:
                companion = next((s for s in document.styles if s.style_id == linked.get(qn("w:val"))), None)
                if companion is not None:
                    companion.font.name = style.font.name
                    companion.font.size = style.font.size
                    companion.font.bold = style.font.bold
                    companion.font.color.rgb = RGBColor(0, 0, 0)
    for style in document.styles:
        fonts = style.element.find(".//" + qn("w:rFonts"))
        if fonts is not None and fonts.get(qn("w:ascii")):
            for attribute in ("asciiTheme", "hAnsiTheme", "eastAsiaTheme", "cstheme"):
                fonts.attrib.pop(qn("w:" + attribute), None)
    for section in document.sections:
        section.page_width, section.page_height = Cm(21), Cm(29.7)
        section.top_margin = section.bottom_margin = Cm(2.5)
        section.left_margin = section.right_margin = Cm(2.5)
        section.footer_distance = Cm(1.25)
        footer = section.footer.paragraphs[0]
        footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
        field = OxmlElement("w:fldSimple")
        field.set(qn("w:instr"), "PAGE")
        footer._p.append(field)
    document.save(Path(__file__).with_name("reference.docx"))


if __name__ == "__main__":
    build()
