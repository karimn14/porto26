import os
import re

files_to_update = [
    r"d:\project\porto26\index.html",
    r"d:\project\porto26\Portfolio.html",
    r"d:\project\porto26\project\index.html",
    r"d:\project\porto26\project\Portfolio.html"
]

for fpath in files_to_update:
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the <!-- LEARNING JOURNAL --> section up to its </section>
    learning_pattern = re.compile(
        r'(<!--\s*LEARNING JOURNAL\s*-->\s*<section id="learning".*?</section>)',
        re.DOTALL
    )

    match = learning_pattern.search(content)
    if match:
        original_section = match.group(1)
        archived_section = f"""<!-- ARCHIVED: LEARNING JOURNAL (Preserved in repository, hidden from public UI) -->
<!--
{original_section}
-->"""
        content = content.replace(original_section, archived_section, 1)

    # Update Contact section numbering from 07 to 06
    content = content.replace('<section id="contact" class="contact" data-num="07">', '<section id="contact" class="contact" data-num="06">')
    content = content.replace('<div class="side-label">07 / Signal Out</div>', '<div class="side-label">06 / Signal Out</div>')
    content = content.replace('<span class="sec-num">07</span>\n      <span class="sec-kicker">Contact / Outbound Channel</span>', '<span class="sec-num">06</span>\n      <span class="sec-kicker">Contact / Outbound Channel</span>')
    content = content.replace('<span class="sec-num">07</span>\r\n      <span class="sec-kicker">Contact / Outbound Channel</span>', '<span class="sec-num">06</span>\r\n      <span class="sec-kicker">Contact / Outbound Channel</span>')

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Archived learning journal in: {fpath}")

print("Done! Learning journal is now hidden from UI while all files remain preserved.")

