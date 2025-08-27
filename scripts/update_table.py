import os
import re

# Root directory where problems are stored
ROOT_DIR = "."

def extract_problem_info(filename):
    # Match pattern like 1-two-sum.java or 1395-minimum-time-visiting-all-points.py
    match = re.match(r"(\d+)-([a-z0-9\-]+)\..*", filename)
    if match:
        num, raw_name = match.groups()
        # Convert "minimum-time-visiting-all-points" → "Minimum Time Visiting All Points"
        name_parts = raw_name.split("-")
        title = " ".join(word.capitalize() for word in name_parts)
        return int(num), title
    return None

def collect_problems():
    problems = []
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if re.match(r"\d+-.*\..*", file):  # Matches files starting with number
                info = extract_problem_info(file)
                if info:
                    problems.append(info)
    return sorted(problems, key=lambda x: x[0])

def generate_table(problems):
    header = "| # | Problem |\n|---|----------|\n"
    rows = [f"| {num} | {title} |" for num, title in problems]
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
