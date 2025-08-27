import os
from pathlib import Path
import re

# Paths
SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parent.parent
README_PATH = REPO_ROOT / "README.md"

# Regex: match files starting with number and dash
FILENAME_RE = re.compile(r"^(\d+-.+)$")

def collect_problem_files():
    found = []
    for f in os.listdir(REPO_ROOT):
        m = FILENAME_RE.match(f)
        if m:
            full_path = REPO_ROOT / f
            rel_path = os.path.relpath(full_path, REPO_ROOT).replace(os.sep, "/")
            found.append((f, rel_path))  # filename as title
    # sort by problem number (numeric prefix)
    found.sort(key=lambda x: int(x[0].split("-")[0]))
    return found

def generate_table_md(problems):
    header = "| # | Problem | Solution |\n|---|----------|----------|\n"
    rows = [f"| {filename.split('-')[0]} | {filename} | [{filename}]({rel_path}) |" for filename, rel_path in problems]
    if not rows:
        rows = ["|  | No problems found |  |"]
    return header + "\n".join(rows)

def update_readme(table_md):
    if not README_PATH.exists():
        print(f"ERROR: README.md not found at {README_PATH}")
        return
    content = README_PATH.read_text(encoding="utf-8")
    start_marker = "<!-- START_TABLE -->"
    end_marker = "<!-- END_TABLE -->"
    new_block = start_marker + "\n" + table_md + "\n" + end_marker
    if start_marker in content and end_marker in content:
        import re
        new_content = re.sub(re.escape(start_marker)+r".*?"+re.escape(end_marker), new_block, content, flags=re.S)
        README_PATH.write_text(new_content, encoding="utf-8")
        print(f"Updated README.md: inserted table with {len(problems)} problems.")
    else:
        README_PATH.write_text(content + "\n" + new_block, encoding="utf-8")
        print(f"Appended table to README.md with {len(problems)} problems.")

if __name__ == "__main__":
    problems = collect_problem_files()
    table_md = generate_table_md(problems)
    update_readme(table_md)
