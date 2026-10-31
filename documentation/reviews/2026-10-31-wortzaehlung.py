"""Count prose in the six main notebooks; never executes notebook code."""
import argparse
import html
import json
import re
from pathlib import Path

FILES = ["index.ipynb", "notebooks/Einleitung.ipynb", "notebooks/Theorie.ipynb",
         "notebooks/Methodik.ipynb", "notebooks/Analyse.ipynb", "notebooks/Fazit.ipynb"]


def prose(source):
    source = re.sub(r"```[^\n]*\n.*?```", " ", source, flags=re.S)
    source = re.sub(r"~~~[^\n]*\n.*?~~~", " ", source, flags=re.S)
    source = re.sub(r"<pre\b.*?</pre>", " ", source, flags=re.S | re.I)
    source = re.sub(r"<h[1-6]\b.*?</h[1-6]>", " ", source, flags=re.S | re.I)
    source = re.sub(r"^\s*#{1,6}\s+.*$", " ", source, flags=re.M)
    source = re.sub(r"^\s*\|.*$", " ", source, flags=re.M)
    source = re.sub(r"^\s*:\s+.*$", " ", source, flags=re.M)
    source = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", source)
    source = re.sub(r"\$\$.*?\$\$", " ", source, flags=re.S)
    source = re.sub(r"(?<!\\)\$(?!\$).*?(?<!\\)\$", " ", source, flags=re.S)
    source = re.sub(r"\[[^\[\]]*@[\w][^\]]*\]", " ", source)
    source = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", source)
    source = re.sub(r"@(sec|fig|tbl|eq)-[\w-]+", " ", source)
    source = re.sub(r"\{\{<.*?>\}\}", " ", source, flags=re.S)
    source = re.sub(r"\{#[^}]+\}", " ", source)
    source = re.sub(r"<!--.*?-->", " ", source, flags=re.S)
    source = re.sub(r"<[^>]+>", " ", source)
    return html.unescape(source)


def count(notebooks):
    rows = []
    for name in FILES:
        text = "\n".join(prose("".join(c.get("source", [])))
                         for c in notebooks[name]["cells"] if c["cell_type"] == "markdown")
        tokens = re.findall(r"\b\w+(?:[’'-]\w+)*\b", text)
        rows.append({"file": name, "word_number_tokens": len(tokens),
                     "tokens_with_letters": sum(any(ch.isalpha() for ch in t) for t in tokens)})
    return {"chapters": rows,
            "with_overview": sum(r["word_number_tokens"] for r in rows),
            "without_overview": sum(r["word_number_tokens"] for r in rows[1:]),
            "with_overview_letters": sum(r["tokens_with_letters"] for r in rows)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--snapshot", type=Path)
    args = parser.parse_args()
    notebooks = json.loads(args.snapshot.read_text(encoding="utf-8")) if args.snapshot else {
        name: json.loads((args.root / name).read_text(encoding="utf-8")) for name in FILES}
    print(json.dumps(count(notebooks), ensure_ascii=False, indent=2))
