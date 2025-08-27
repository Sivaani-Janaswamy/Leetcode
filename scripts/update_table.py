#!/usr/bin/env python3
import os
import re
from pathlib import Path
import sys

# ---------- CONFIG ----------
SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parent.parent   # assumes scripts/ is one level under repo root
README_PATH = REPO_ROOT / "README.md"

# extensions to look for (add more if needed)
EXTENSIONS = ("java","py","cpp","c","js","ts","cs","rb","go","kt","swift")

# regex to match filenames like "1-two-sum.py" or "1395-minimum-time-visiting-all-points.java"
EXT_PATTERN = "|".join(map(re.escape, EXTENSIONS))
FILENAME_RE = re.compile(rf"^(\d+)-([a-z0-9][a-z0-9\-\_]*)\.({EXT_PATTERN})$", re.I)
# -----------------------------

def collect_problem_files():
    found = []
    for root, dirs, files in os.walk(REPO_ROOT):
        # skip git internals and workflow folder to speed things up
        if ".git" in root.split(os.sep) or ".github" in root.split(os.sep):
            continue
        for f in files:
            m = FILENAME_RE.match(f)
            if m:
                num = int(m.group(1))
                raw = m.group(2)
                ext = m.group(3).lower()
                title = raw.replace("-", " ").replace("_", " ").title()
                full_path = Path(root) / f
                rel_path = os.path.relpath(full_path, REPO_ROOT).replace(os.sep, "/")
                found.append((num, title, rel_path, ext))
    # sort by numeric problem number then by filename (stable)
    found.sort(key=lambda x: (x[0], x[2]))
    return found

def generate_table_md(problems):
    header = "| # | Problem | Solution |\n|---:|---|---|\n"
    rows = []
    for num, title, rel, ext in problems:
        filename = os.path.basename(rel)
        rows.append(f"| {num} | {title} | [{filename}]({rel}) |")
    if not rows:
        rows = ["|  | No problems found matching `^<number>-<name>.<ext>` |  |"]
    return header + "\n".join(rows)

def update_readme_with_table(table_md, problems_count):
    if not README_PATH.exists():
        print(f"ERROR: README.md not found at {README_PATH}")
        sys.exit(1)

    content = README_PATH.read_text(encoding="utf-8")
    start_marker = "<!-- START_TABLE -->"
    end_marker = "<!-- END_TABLE -->"

    new_table_block = start_marker + "\n" + table_md + "\n" + end_marker

    if start_marker in content and end_marker in content:
        # replace the existing block
        new_content = re.sub(
            re.escape(start_marker) + r".*?" + re.escape(end_marker),
            new_table_block,
            content,
            flags=re.S
        )
        README_PATH.write_text(new_content, encoding="utf-8")
        print(f"Updated README.md: inserted table with {problems_count} problems.")
    else:
        # fallback: append markers + table at the end
        if not content.endswith("\n"):
            content += "\n"
        content += "\n" + new_table_block + "\n"
        README_PATH.write_text(content, encoding="utf-8")
        print(f"Appended table to README.md (no markers found). Inserted {problems_count} problems.")

if __name__ == "__main__":
    problems = collect_problem_files()
    print(f"DEBUG: Found {len(problems)} problem file(s). (showing up to 20)")
    for item in problems[:20]:
        print("  ", item)
    table_md = generate_table_md(problems)
    update_readme_with_table(table_md, len(problems))
