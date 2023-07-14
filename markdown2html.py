#!/usr/bin/python3
"""
Script that converts a Markdown file to HTML.
"""

import sys
import os.path
import re

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read the input Markdown file
    with open(input_file, 'r') as f:
        markdown = f.read()

    # Convert Markdown headings to HTML
    html = re.sub(r'^(#+)\s(.+)$', lambda m: f"<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>", markdown, flags=re.MULTILINE)

    # Write the HTML to the output file
    with open(output_file, 'w') as f:
        f.write(html)

    sys.exit(0)
