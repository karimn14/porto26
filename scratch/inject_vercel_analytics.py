import os

script_tag = """  <!-- Vercel Web Analytics -->
  <script>
    window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
  </script>
  <script defer src="/_vercel/insights/script.js"></script>
"""

base_dir = r"d:\project\porto26"
count = 0
for root, dirs, files in os.walk(base_dir):
    # skip .git and scratch
    if ".git" in root or "scratch" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            fpath = os.path.join(root, file)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            
            if "/_vercel/insights/script.js" not in content:
                if "</head>" in content:
                    new_content = content.replace("</head>", script_tag + "</head>", 1)
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    count += 1
                    rel = os.path.relpath(fpath, base_dir)
                    print("Injected analytics into:", rel)

print("Total HTML files updated with Vercel Analytics:", count)

