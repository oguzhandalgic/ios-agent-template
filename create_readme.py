# generate_readme_from_yaml.py
"""
Generates README.md from readme-template.yaml
Usage: python generate_readme_from_yaml.py [path_to_yaml]
"""

import yaml
import sys
from pathlib import Path


def generate_section(section):
    lines = []
    title = section.get('title', '')
    if title:
        lines.append(f"## {title}\n")

    s_type = section['type']

    if s_type == 'features':
        for item in section.get('items', []):
            if isinstance(item, str):
                lines.append(f"- {item}")
            elif isinstance(item, dict):
                for key, sublist in item.items():
                    lines.append(f"- {key}")
                    for sub in sublist:
                        lines.append(f"  - {sub}")
        lines.append("")

    elif s_type == 'structure':
        lines.append("```text")
        lines.append(section.get('code_block', '').strip())
        lines.append("```\n")

    elif s_type == 'quickstart':
        for step in section.get('steps', []):
            lines.append(step['text'])
            if 'subtext' in step:
                lines.append(step['subtext'])
            if 'code' in step:
                lines.append("```bash")
                lines.append(step['code'].strip())
                lines.append("```")
            if 'items' in step:
                for item in step['items']:
                    lines.append(f"- {item}")
            if 'note' in step:
                lines.append(f"→ {step['note']}\n")

    elif s_type == 'workflow_diagram':
        lines.append("```text")
        lines.append(section.get('diagram', '').strip())
        lines.append("```\n")

    elif s_type == 'table':
        headers = section['headers']
        rows = section['rows']
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
        for row in rows:
            lines.append("| " + " | ".join(row) + " |")
        lines.append("")

    elif s_type == 'list':
        for item in section.get('items', []):
            lines.append(f"- {item}")
        lines.append("")

    elif s_type == 'todo':
        for item in section.get('items', []):
            lines.append(f"- [ ] {item}")
        lines.append("")

    elif s_type == 'text':
        lines.append(section.get('content', '').strip() + "\n")

    return lines


def main(yaml_path_str="readme-template.yaml"):
    yaml_path = Path(yaml_path_str)
    if not yaml_path.exists():
        print(f"Error: YAML file not found: {yaml_path}")
        sys.exit(1)

    try:
        with yaml_path.open(encoding="utf-8") as f:
            data = yaml.safe_load(f)

        readme = data["readme"]
        output_lines = []

        # Title + subtitle
        output_lines.append(f"# {readme['title']}")
        output_lines.append(f"**{readme['subtitle']}**\n")

        # Badges
        for badge in readme.get("badges", []):
            output_lines.append(f"![{badge['name']}]({badge['url']})")
        output_lines.append("")

        # Description
        output_lines.append(readme["description"].strip() + "\n")

        # Generate all sections
        for section in readme.get("sections", []):
            output_lines.extend(generate_section(section))

        # Write final file
        readme_path = Path("README.md")
        readme_path.write_text("\n".join(output_lines), encoding="utf-8")
        print(f"Successfully generated: {readme_path.absolute()}")

    except Exception as e:
        print(f"Error generating README: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()