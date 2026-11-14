"""Build the English index.html from the Japanese one.

Usage: python3 tools/build_en.py ../sudoku/index.html index.html

Each file in tools/strings/ defines P = [(japanese, english[, count]), ...].
Every Japanese string must appear exactly `count` times (default 1); any that
don't are listed so the tables can be updated after the Japanese app changes.
"""
import importlib.util, pathlib, re, sys

src, dst = sys.argv[1], sys.argv[2]
text = pathlib.Path(src).read_text(encoding="utf-8")
missing = 0
for f in sorted((pathlib.Path(__file__).parent / "strings").glob("*.py")):
    spec = importlib.util.spec_from_file_location(f.stem, f)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for entry in mod.P:
        old, new = entry[0], entry[1]
        want = entry[2] if len(entry) > 2 else 1
        got = text.count(old)
        if got != want:
            print(f"{f.name}: expected {want}, found {got}: {old[:100]}")
            missing += 1
            continue
        text = text.replace(old, new)
# Separate localStorage keys from the Japanese app (same origin). File format id "sudoku-board" stays.
text = re.sub(r'"sudoku-(?!board")([a-z0-9-]+)"', r'"numplace-en-\1"', text)
pathlib.Path(dst).write_text(text, encoding="utf-8")
left = [i for i, l in enumerate(text.splitlines(), 1)
        if re.search(r'["`>][^"`<>\n]*[぀-ヿ一-鿿＀-￯]', l) and not l.lstrip().startswith(("//", "/*"))]
print(f"{missing} strings not found; lines that may still contain Japanese text: {len(left)}")
sys.exit(1 if missing else 0)
