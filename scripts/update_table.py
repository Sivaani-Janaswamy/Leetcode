import os
import re

# Root directory where problems are stored
ROOT_DIR = "."

def extract_problem_info(filename):
    match = re.match(r"(\d+)_([A-Za-z0-9]+)_(Easy|Medium|Hard)", filename)
    if match:
        num, name, diff = match.groups()
        # Convert CamelCase/NoSpaces → Proper Spacing
        name = re.sub(r"([a-z])([A-Z])", r"\1 \2", name)
        name = name.replace("_", " ")
        return int(num), name, diff
    return None

def collect_problems():
    problems = []
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if re.match(r"\d+_.*_(Easy|Medium|Hard)\..*", file):
                info = extract_problem_info(file)
                if info:
                    problems.append(info)
    return sorted(problems, key=lambda x: x[0])

def generate_table(problems):
    header = "| # | Problem | Difficulty |\n|---|----------|-------------|\n"
    rows = [f"| {num} | {title} | {diff} |" for num, title, diff in problems]
    return header + "\n".join(rows)

def update_readme(problems):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    table = generate_table(problems)
    new_content = re.sub(
        r"(?s)(<!-- START_TABLE -->)(.*?)(<!-- END_TABLE -->)",
        f"<!-- START_TABLE -->\n{table}\n<!-- END_TABLE -->",
        content
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    problems = collect_problems()
    update_readme(problems)
