import os
import re

ROOT_DIR = "."

def extract_problem_info(filename):
    # Match filenames like 1-two-sum.java OR 2_add_two_numbers.py
    match = re.match(r"(\d+)[-_](.+)\.(java|py|cpp)$", filename)
    if match:
        num, raw_name, _ = match.groups()
        # Convert to proper spacing + capitalization
        name = raw_name.replace("-", " ").replace("_", " ").title()
        return int(num), name
    return None

def collect_problems():
    problems = []
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if re.match(r"\d+[-_].*\.(java|py|cpp)$", file):
                info = extract_problem_info(file)
                if info:
                    problems.append(info)
    return sorted(problems, key=lambda x: x[0])

def generate_table(problems):
    header = "| # | Problem | Solution |\n|---|----------|----------|\n"
    rows = [f"| {num} | {title} | [{title}]({file}) |" 
            for num, title in problems 
            for file in os.listdir(ROOT_DIR) 
            if file.startswith(str(num))]  # link the correct file
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
