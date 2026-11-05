import os

files = [
    r"d:\project\porto26\index.html",
    r"d:\project\porto26\Portfolio.html",
    r"d:\project\porto26\project\index.html",
    r"d:\project\porto26\project\Portfolio.html"
]

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    mobile_target = '<a href="#" data-close>Download CV ↗</a>'
    mobile_replacement = '<a href="#" data-close>Download CV ↗</a>\n  <a href="javascript:void(0)" onclick="window.toggleLanguage()" id="mobileLangToggle" style="color:var(--accent); font-family:var(--mono); font-size:16px;">🌐 <span id="mobileLangText">한국어 (KO)</span></a>'

    if 'id="mobileLangToggle"' not in content and mobile_target in content:
        content = content.replace(mobile_target, mobile_replacement, 1)

    # Also update translations in script to handle mobileLangText
    if 'const mobileText = document.getElementById("mobileLangText");' not in content:
        old_hook = 'const navBtnText = document.getElementById(\'navLangText\');'
        new_hook = '''const navBtnText = document.getElementById('navLangText');
    const mobileText = document.getElementById('mobileLangText');
    if(mobileText) mobileText.textContent = lang === 'en' ? '한국어 (KO)' : 'English (EN)';'''
        content = content.replace(old_hook, new_hook)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Added mobile language toggle to: {fpath}")

print("Mobile toggle added!")

