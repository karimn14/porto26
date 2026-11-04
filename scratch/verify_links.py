import os
import re

files = [
    r'd:\project\porto26\index.html',
    r'd:\project\porto26\Portfolio.html',
    r'd:\project\porto26\project\index.html',
    r'd:\project\porto26\project\Portfolio.html'
]
for p in os.listdir(r'd:\project\porto26\projects'):
    if p.endswith('.html'):
        files.append(os.path.join(r'd:\project\porto26\projects', p))
for p in os.listdir(r'd:\project\porto26\project\projects'):
    if p.endswith('.html'):
        files.append(os.path.join(r'd:\project\porto26\project\projects', p))

broken_images = 0
broken_links = 0

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
        
    base_dir = os.path.dirname(fpath)
    
    # check images
    imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', text)
    for img in imgs:
        if img.startswith('http') or img.startswith('data:'):
            continue
        resolved = os.path.normpath(os.path.join(base_dir, img))
        if not os.path.exists(resolved):
            print(f'MISSING IMAGE in {os.path.basename(fpath)}: {img} -> {resolved}')
            broken_images += 1
            
    # check internal hrefs (e.g. projects/*.html)
    hrefs = re.findall(r'<a[^>]+href=[\'"]([^\'"]+)[\'"]', text)
    for h in hrefs:
        if h.startswith('http') or h.startswith('#') or h.startswith('mailto:') or h.startswith('tel:'):
            continue
        clean_h = h.split('#')[0]
        if clean_h:
            resolved = os.path.normpath(os.path.join(base_dir, clean_h))
            if not os.path.exists(resolved):
                print(f'MISSING LINK in {os.path.basename(fpath)}: {h} -> {resolved}')
                broken_links += 1

print(f"Audit completed: {len(files)} files checked.")
print(f"Total broken image links: {broken_images}")
print(f"Total broken page links: {broken_links}")

