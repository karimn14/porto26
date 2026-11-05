import os

files = [
    r"d:\project\porto26\index.html",
    r"d:\project\porto26\Portfolio.html",
    r"d:\project\porto26\project\index.html",
    r"d:\project\porto26\project\Portfolio.html"
]

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = content.replace('href="javascript:void(0)" onclick="window.toggleLanguage()"', 'href="#" onclick="window.toggleLanguage(); return false;"')

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Fixed href javascript:void(0)")
