import os
import re

def split_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    sections = re.split(r'(?m)^# (.+)', content)
    for i in range(1, len(sections), 2):
        section_name = sections[i].strip().replace("\\_", "_")
        section_content = sections[i + 1].strip()
        card_content = f"""---
title: {section_name}
---

{section_content}
"""
        file_name = f"{section_name}.mdx"
        output_file = os.path.join("./docs", file_name)
        with open(output_file, 'w', encoding='utf-8') as new_file:
            new_file.write(card_content)
        print(f"File '{file_name}' created.")
        
if __name__ == "__main__":
    split_markdown('./docs/README.md')
