import os
import re

ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
README_PATH = os.path.join(ROOT_DIR, "README.md")

def extract_problem_info(filename):
    match = re.match(r"(\d+)-([a-z0-9\-]+)\..*", filename)
    if match:
        num, raw_name = match.groups()
        title = " ".join(word.capitalize() for word in raw_name.split("-"))
        return int(num), title, filename
    return None

def collect_problems():
    problems = []
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if re.match(r"\d+-.*\..*", file):
                info = extract_problem_info(file)
                if info:
                    problems.append(info)
    return sorted(problems, key=lambda x: x[0])

def generate_table(problems):
    header = "| # | Problem | Solution |\n|---|----------|----------|\n"
    rows = [
        f"| {num} | {title} | [{file}](./{file}) |"
        for num, title, file in problems
    ]
    return header + "\n".join(rows)

def update_readme(problems):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    table = generate_table(problems)
    new_content = re.sub(
        r"(?s)(<!-- START_TABLE -->)(.*?)(<!-- END_TABLE -->)",
        f"<!-- START_TABLE -->\n{table}\n<!-- END_TABLE -->",
        content
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    problems = collect_problems()
    update_readme(problems)
