import os
import sys

# Target directories
projects_dir = r"d:\project\porto26\projects"
project_projects_dir = r"d:\project\porto26\project\projects"

os.makedirs(projects_dir, exist_ok=True)
os.makedirs(project_projects_dir, exist_ok=True)

# Delete obsolete project files
obsolete_slugs = [
    "company-landing-pages",
    "free-healthy-meal-webapp",
    "gic-power-system",
    "bridge-faulty-sensor-fft",
    "mpc-leso-etc-quadrotor" # renamed to l1-adaptive-control-uav
]

for slug in obsolete_slugs:
    p1 = os.path.join(projects_dir, f"{slug}.html")
    p2 = os.path.join(project_projects_dir, f"{slug}.html")
    if os.path.exists(p1):
        os.remove(p1)
        print(f"Removed {p1}")
    if os.path.exists(p2):
        os.remove(p2)
        print(f"Removed {p2}")

# Common HTML template builder
def build_html(data):
    slug = data["slug"]
    title = data["title"]
    subtitle = data["subtitle"]
    role = data["role"]
    client = data["client"]
    period = data["period"]
    stack_str = data["stack_str"]
    case_num = data["case_num"]
    metrics = data["metrics"]
    sections = data["sections"]
    
    hero_svg = data["hero_svg"]
    arch_svg = data["arch_svg"]
    fig2_svg = data["fig2_svg"]
    gallery_svgs = data["gallery_svgs"]
    
    body_content = data["body_content"]
    stack_chips = data["stack_chips"]
    
    prev_link = data.get("prev_link", "../index.html#projects")
    next_link = data.get("next_link", "../index.html#projects")
    
    metrics_html = "".join([f'''
        <div class="metric">
          <div class="n">{val}</div>
          <div class="lbl">{lbl}</div>
        </div>''' for val, lbl in metrics])

    sections_aside = "".join([f'''
        <li><a href="#{sec_id}"><span class="num">{idx+1:02d}</span><span>{sec_title}</span></a></li>''' 
        for idx, (sec_id, sec_title) in enumerate(sections)])

    chips_html = "".join([f'<span class="t">{t}</span>' for t in stack_chips])

    gallery_html = "".join([f'''
        <div class="frame">
          {g_svg}
          <image-slot id="{slug}-g{idx+1}" shape="rect" placeholder="Gallery view {idx+1}"></image-slot>
        </div>''' for idx, g_svg in enumerate(gallery_svgs)])

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title} — Project Detail · Nabil Karim</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;400;500;600;700&family=DM+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
<script src="../image-slot.js"></script>
<style>
  :root{{
    --bg:#090909;
    --surface:#111111;
    --fg:#EDEDED;
    --muted:#666666;
    --divider:#1C1C1C;
    --accent:#F05E1C;
    --accent-glow:rgba(240,94,28,0.35);
    --mono:"IBM Plex Mono", ui-monospace, monospace;
    --sans:"DM Sans", system-ui, sans-serif;
    --gutter:clamp(20px, 5vw, 80px);
    --maxw:1280px;
  }}
  *{{box-sizing:border-box;margin:0;padding:0;}}
  html{{scroll-behavior:smooth;}}
  body{{
    background:var(--bg); color:var(--fg);
    font-family:var(--sans); line-height:1.6;
    -webkit-font-smoothing:antialiased;
    background-image:
      linear-gradient(rgba(237,237,237,0.018) 1px, transparent 1px),
      linear-gradient(90deg, rgba(237,237,237,0.018) 1px, transparent 1px);
    background-size: 48px 48px;
    background-attachment: fixed;
    cursor:none;
  }}
  body::before{{
    content:""; position:fixed; inset:0;
    pointer-events:none; z-index:9998;
    background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 0.55 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)' opacity='0.18'/></svg>");
    mix-blend-mode:overlay; opacity:0.5;
  }}
  ::selection{{background:var(--accent); color:#000;}}

  .cursor{{
    position:fixed; top:0; left:0;
    width:18px; height:18px;
    pointer-events:none; z-index:9999;
    transform:translate(-50%,-50%);
    transition:opacity .15s ease, transform .08s linear;
  }}
  .cursor::before, .cursor::after{{
    content:""; position:absolute; background:var(--accent);
    box-shadow:0 0 8px var(--accent-glow);
  }}
  .cursor::before{{ left:50%; top:0; bottom:0; width:1px; transform:translateX(-50%); }}
  .cursor::after{{ top:50%; left:0; right:0; height:1px; transform:translateY(-50%); }}
  .cursor .dot{{
    position:absolute; left:50%; top:50%;
    width:4px; height:4px; background:var(--accent);
    border-radius:50%; transform:translate(-50%,-50%);
    box-shadow:0 0 6px var(--accent-glow);
  }}
  .cursor.hover{{ transform:translate(-50%,-50%) scale(1.6); }}
  @media (hover:none){{ body{{ cursor:auto; }} .cursor{{ display:none; }} }}

  nav.top{{
    position:fixed; top:0; left:0; right:0; z-index:100;
    padding:18px 0;
    background:rgba(9,9,9,0.72);
    backdrop-filter:blur(14px) saturate(140%);
    border-bottom:1px solid var(--divider);
  }}
  nav.top .wrap{{
    max-width:var(--maxw); margin:0 auto; padding:0 var(--gutter);
    display:flex; align-items:center; justify-content:space-between;
  }}
  .brand{{
    font-family:var(--mono); font-weight:700; font-size:18px;
    color:var(--fg); text-decoration:none; display:inline-flex; align-items:baseline; gap:2px;
  }}
  .brand .dot{{
    width:6px; height:6px; background:var(--accent); border-radius:50%;
    display:inline-block; margin-left:3px; box-shadow:0 0 8px var(--accent-glow);
  }}
  .back{{
    font-family:var(--mono); font-size:11px; letter-spacing:0.18em; text-transform:uppercase;
    color:var(--fg); text-decoration:none;
    display:inline-flex; align-items:center; gap:8px; cursor:none;
  }}
  .back .arr{{ color:var(--accent); transition:transform .2s ease; }}
  .back:hover .arr{{ transform:translateX(-4px); }}

  .wrap{{ max-width:var(--maxw); margin:0 auto; padding:0 var(--gutter); }}

  .case-hero{{ padding:160px 0 60px; }}
  .breadcrumbs{{
    display:flex; gap:14px; align-items:center;
    font-family:var(--mono); font-size:11px; letter-spacing:0.18em; text-transform:uppercase;
    color:var(--muted); margin-bottom:32px;
  }}
  .breadcrumbs a{{ color:var(--muted); text-decoration:none; }}
  .breadcrumbs a:hover{{ color:var(--accent); }}
  .breadcrumbs .sep{{ color:var(--divider); }}
  .breadcrumbs .cur{{ color:var(--accent); }}

  .case-title{{
    font-family:var(--mono); font-weight:500;
    font-size:clamp(32px, 5.5vw, 68px);
    line-height:1.05; letter-spacing:-0.025em;
    color:var(--fg); margin-bottom:32px; max-width:24ch; text-wrap:pretty;
  }}
  .case-title .glow{{ color:var(--accent); text-shadow:0 0 24px rgba(240,94,28,0.4); }}

  .case-deck{{
    font-size:17.5px; color:var(--fg); opacity:0.82; line-height:1.6;
    max-width:64ch; margin-bottom:48px;
  }}

  .case-spec{{
    display:grid; grid-template-columns:repeat(4, 1fr); gap:0;
    border-top:1px solid var(--divider); border-bottom:1px solid var(--divider);
  }}
  .spec-cell{{ padding:18px 22px 18px 0; border-right:1px solid var(--divider); }}
  .spec-cell:last-child{{ border-right:none; padding-right:0; }}
  .spec-cell:nth-child(n+2){{ padding-left:22px; }}
  .spec-cell .k{{
    font-family:var(--mono); font-size:10px; letter-spacing:0.22em; text-transform:uppercase;
    color:var(--accent); opacity:0.7; margin-bottom:6px;
  }}
  .spec-cell .v{{
    font-family:var(--mono); font-size:13px; color:var(--fg); letter-spacing:0.02em;
  }}
  @media (max-width:760px){{
    .case-spec{{ grid-template-columns:1fr 1fr; }}
    .spec-cell{{ padding:14px 16px; border-right:1px solid var(--divider); }}
    .spec-cell:nth-child(2n){{ border-right:none; }}
    .spec-cell:nth-child(n+3){{ border-top:1px solid var(--divider); }}
  }}

  .cover-large{{
    margin:60px 0 80px; width:100%; aspect-ratio:16/9;
    border:1px solid var(--divider);
    background:
      repeating-linear-gradient(45deg, rgba(237,237,237,0.025) 0 1px, transparent 1px 12px),
      #0d0d0d;
    position:relative; overflow:hidden;
    display:flex; align-items:center; justify-content:center;
  }}
  .cover-large image-slot{{ position:absolute; inset:0; width:100%; height:100%; --slot-bg:transparent; --slot-border:transparent; z-index:3; }}
  .cover-large .svg-bg{{ position:absolute; inset:0; width:100%; height:100%; z-index:1; pointer-events:none; }}
  .cover-large::before, .cover-large::after{{
    content:""; position:absolute; width:18px; height:18px;
    border:1px solid var(--accent); pointer-events:none; z-index:4;
  }}
  .cover-large::before{{ top:-1px; left:-1px; border-right:none; border-bottom:none; }}
  .cover-large::after{{ bottom:-1px; right:-1px; border-left:none; border-top:none; }}

  .content{{ display:grid; grid-template-columns: 200px 1fr; gap:60px; padding-bottom:80px; }}
  .content aside{{
    position:sticky; top:120px; align-self:start;
    font-family:var(--mono); font-size:11px; letter-spacing:0.06em;
  }}
  .content aside .lbl{{
    font-size:10px; letter-spacing:0.22em; text-transform:uppercase;
    color:var(--accent); opacity:0.7; margin-bottom:14px;
  }}
  .content aside ul{{ list-style:none; }}
  .content aside li{{ padding:8px 0; border-bottom:1px solid var(--divider); }}
  .content aside a{{
    color:var(--fg); opacity:0.7; text-decoration:none; display:flex; gap:10px;
    transition:color .2s ease, opacity .2s ease;
  }}
  .content aside a:hover{{ color:var(--accent); opacity:1; }}
  .content aside a .num{{ color:var(--accent); opacity:0.55; }}

  .body{{ max-width:68ch; }}
  .body h2{{
    font-family:var(--mono); font-weight:600; font-size:24px; line-height:1.3; letter-spacing:-0.01em;
    color:var(--fg); margin:48px 0 18px; display:flex; align-items:baseline; gap:14px;
  }}
  .body h2 .num{{ color:var(--accent); opacity:0.5; font-size:13px; letter-spacing:0.18em; min-width:36px; }}
  .body h3{{ font-family:var(--mono); font-weight:500; font-size:15px; color:var(--accent); margin:32px 0 10px; letter-spacing:0.04em; }}
  .body p{{ font-size:16px; color:var(--fg); margin-bottom:22px; line-height:1.75; opacity:0.9; }}
  .body p strong{{ color:var(--accent); font-family:var(--mono); font-size:0.96em; font-weight:600; }}
  .body em{{ color:var(--fg); font-style:italic; }}
  .body ul{{ list-style:none; margin:0 0 22px 0; }}
  .body ul li{{
    font-size:15.5px; padding-left:28px; position:relative; margin-bottom:10px; line-height:1.7;
    color:var(--fg); opacity:0.88;
  }}
  .body ul li::before{{ content:"▸"; position:absolute; left:0; top:0; color:var(--accent); font-family:var(--mono); font-size:13px; }}

  .metrics{{ display:grid; grid-template-columns:repeat(3, 1fr); gap:14px; margin:36px 0 24px; }}
  .metric{{ padding:22px 20px; border:1px solid var(--divider); background:var(--surface); position:relative; overflow:hidden; }}
  .metric::before{{ content:""; position:absolute; top:0; left:0; right:0; height:2px; background:var(--accent); opacity:0.7; }}
  .metric .n{{
    font-family:var(--mono); font-weight:600; font-size:28px; color:var(--accent);
    line-height:1.1; margin-bottom:8px; letter-spacing:-0.02em; text-shadow:0 0 12px rgba(240,94,28,0.25);
  }}
  .metric .lbl{{ font-family:var(--mono); font-size:10px; letter-spacing:0.2em; text-transform:uppercase; color:var(--muted); }}
  @media (max-width:760px){{ .metrics{{ grid-template-columns:1fr; }} }}

  .figure{{ margin:36px 0; }}
  .figure .frame{{
    width:100%; aspect-ratio:16/10; border:1px solid var(--divider);
    background: repeating-linear-gradient(45deg, rgba(237,237,237,0.025) 0 1px, transparent 1px 10px), #0d0d0d;
    position:relative; overflow:hidden; display:flex; align-items:center; justify-content:center;
  }}
  .figure .frame svg{{ position:absolute; inset:0; width:100%; height:100%; z-index:1; pointer-events:none; }}
  .figure image-slot{{ position:absolute; inset:0; width:100%; height:100%; --slot-bg:transparent; --slot-border:transparent; z-index:3; }}
  .figure .cap{{ margin-top:10px; font-family:var(--mono); font-size:11px; letter-spacing:0.06em; color:var(--muted); }}
  .figure .cap b{{ color:var(--accent); font-weight:500; margin-right:8px; }}

  .gallery{{ display:grid; grid-template-columns:repeat(3, 1fr); gap:14px; margin:32px 0; }}
  .gallery .frame{{
    aspect-ratio:1/1; position:relative; overflow:hidden; border:1px solid var(--divider); background:#0d0d0d;
    display:flex; align-items:center; justify-content:center;
  }}
  .gallery .frame svg{{ position:absolute; inset:0; width:100%; height:100%; z-index:1; pointer-events:none; }}
  .gallery image-slot{{ position:absolute; inset:0; width:100%; height:100%; --slot-bg:transparent; --slot-border:transparent; z-index:3; }}
  @media (max-width:760px){{ .gallery{{ grid-template-columns:1fr 1fr; }} }}

  .stack-chips{{ display:flex; flex-wrap:wrap; gap:6px; margin:12px 0 28px; }}
  .stack-chips .t{{
    font-family:var(--mono); font-size:11px; color:var(--muted); padding:5px 10px; border:1px solid var(--divider);
    transition:border-color .2s ease, color .2s ease;
  }}
  .stack-chips .t:hover{{ border-color:var(--accent); color:var(--accent); }}

  pre, code{{ font-family:var(--mono); font-size:13px; }}
  pre{{
    background:#0d0d0d; border:1px solid var(--divider); border-left:2px solid var(--accent);
    padding:18px 22px; overflow-x:auto; margin:24px 0 28px; line-height:1.65; color:#cfcfcf;
  }}
  code{{ background:#1a1a1a; padding:2px 6px; color:var(--accent); border-radius:2px; }}
  pre code{{ background:transparent; padding:0; color:inherit; }}

  blockquote{{
    border-left:2px solid var(--accent); padding:8px 0 8px 22px; margin:32px 0;
    font-family:var(--mono); font-size:14.5px; color:var(--fg); opacity:0.88; line-height:1.6; background:rgba(240,94,28,0.03);
  }}

  .case-foot{{ margin-top:60px; padding-top:32px; border-top:1px solid var(--divider); display:flex; flex-direction:column; gap:20px; }}
  .case-foot .author{{ display:flex; align-items:center; gap:12px; font-family:var(--mono); font-size:12px; letter-spacing:0.06em; color:var(--muted); }}
  .case-foot .pip{{ width:6px; height:6px; background:var(--accent); border-radius:50%; box-shadow:0 0 6px var(--accent-glow); }}

  .foot-nav{{
    display:flex; justify-content:space-between; align-items:center; gap:16px;
    margin-top:10px; padding-top:20px; border-top:1px solid var(--divider);
    font-family:var(--mono); font-size:12px; letter-spacing:0.12em; text-transform:uppercase;
  }}
  .foot-nav a{{ color:var(--fg); text-decoration:none; transition:color .2s ease; cursor:none; }}
  .foot-nav a:hover{{ color:var(--accent); }}

  @media (max-width:900px){{
    .content{{ grid-template-columns:1fr; gap:36px; }}
    .content aside{{ position:static; }}
  }}
</style>
</head>
<body>

<div class="cursor" id="cursor"><span class="dot"></span></div>

<nav class="top">
  <div class="wrap">
    <a href="../index.html" class="brand">Nabil Karim<span class="dot"></span></a>
    <a href="../index.html#projects" class="back"><span class="arr">←</span> Back to Portfolio</a>
  </div>
</nav>

<section class="case-hero">
  <div class="wrap">
    <div class="breadcrumbs">
      <a href="../index.html">Portfolio</a>
      <span class="sep">/</span>
      <a href="../index.html#projects">Projects</a>
      <span class="sep">/</span>
      <span class="cur">Case Study {case_num:02d}</span>
    </div>

    <h1 class="case-title">{title}</h1>

    <p class="case-deck">
      {subtitle}
    </p>

    <div class="case-spec">
      <div class="spec-cell">
        <div class="k">Role</div>
        <div class="v">{role}</div>
      </div>
      <div class="spec-cell">
        <div class="k">Client / Context</div>
        <div class="v">{client}</div>
      </div>
      <div class="spec-cell">
        <div class="k">Period</div>
        <div class="v">{period}</div>
      </div>
      <div class="spec-cell">
        <div class="k">Stack</div>
        <div class="v">{stack_str}</div>
      </div>
    </div>
  </div>
</section>

<div class="wrap">
  <div class="cover-large">
    <div class="svg-bg">{hero_svg}</div>
    <image-slot id="{slug}-cover" shape="rect" placeholder="Hero cover photo for {title}"></image-slot>
  </div>

  <div class="content">
    <aside>
      <div class="lbl">Sections</div>
      <ul>
        {sections_aside}
      </ul>
    </aside>

    <main class="body">
      {body_content}

      <div class="metrics">
        {metrics_html}
      </div>

      <h3>Technical Stack &amp; Tools</h3>
      <div class="stack-chips">
        {chips_html}
      </div>

      <div class="case-foot">
        <div class="author">
          <span class="pip"></span>
          <span>Engineering Project Documentation by Nabil Karim · Class of 2026</span>
        </div>
        <div class="foot-nav">
          <a href="{prev_link}">← Previous Project</a>
          <a href="../index.html#projects">All Projects ↑</a>
          <a href="{next_link}">Next Project →</a>
        </div>
      </div>
    </main>
  </div>
</div>

<script>
  (function(){{
    const cursor = document.getElementById('cursor');
    if(!cursor) return;
    let x=0,y=0,tx=0,ty=0;
    document.addEventListener('mousemove', e=>{{ tx=e.clientX; ty=e.clientY; }});
    function loop(){{
      x += (tx-x)*0.35; y += (ty-y)*0.35;
      cursor.style.transform = `translate(${{x}}px, ${{y}}px) translate(-50%,-50%)`;
      requestAnimationFrame(loop);
    }}
    loop();
    document.addEventListener('mousedown', ()=>cursor.classList.add('hover'));
    document.addEventListener('mouseup', ()=>cursor.classList.remove('hover'));
    document.querySelectorAll('a, button, .metric, .stack-chips .t').forEach(el=>{{
      el.addEventListener('mouseenter', ()=>cursor.classList.add('hover'));
      el.addEventListener('mouseleave', ()=>cursor.classList.remove('hover'));
    }});
  }})();
</script>

</body>
</html>
'''
    return html

# SVG helpers
def make_svg_cover(title_text, subtitle_text, icon_symbol="◈"):
    return f'''<svg viewBox="0 0 1200 675" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="background:#090909;">
      <defs>
        <pattern id="cov-grid" width="40" height="40" patternUnits="userSpaceOnUse">
          <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1c1c1c" stroke-width="1"/>
        </pattern>
      </defs>
      <rect width="100%" height="100%" fill="url(#cov-grid)"/>
      <circle cx="600" cy="337" r="240" fill="none" stroke="#1c1c1c" stroke-width="1" stroke-dasharray="4 4"/>
      <circle cx="600" cy="337" r="180" fill="none" stroke="#F05E1C" stroke-width="1" stroke-opacity="0.25"/>
      <circle cx="600" cy="337" r="120" fill="none" stroke="#F05E1C" stroke-width="1.5" stroke-opacity="0.4"/>
      <line x1="100" y1="337" x2="1100" y2="337" stroke="#1c1c1c" stroke-width="1"/>
      <line x1="600" y1="50" x2="600" y2="625" stroke="#1c1c1c" stroke-width="1"/>
      <path d="M 150 150 L 350 150 L 400 200 L 550 200" fill="none" stroke="#F05E1C" stroke-width="2" stroke-opacity="0.6"/>
      <circle cx="350" cy="150" r="4" fill="#F05E1C"/>
      <circle cx="550" cy="200" r="4" fill="#F05E1C"/>
      <path d="M 1050 525 L 850 525 L 800 475 L 650 475" fill="none" stroke="#F05E1C" stroke-width="2" stroke-opacity="0.6"/>
      <circle cx="850" cy="525" r="4" fill="#F05E1C"/>
      <circle cx="650" cy="475" r="4" fill="#F05E1C"/>
      <path d="M 60 90 L 60 60 L 90 60" fill="none" stroke="#F05E1C" stroke-width="2"/>
      <path d="M 1140 90 L 1140 60 L 1110 60" fill="none" stroke="#F05E1C" stroke-width="2"/>
      <path d="M 60 585 L 60 615 L 90 615" fill="none" stroke="#F05E1C" stroke-width="2"/>
      <path d="M 1140 585 L 1140 615 L 1110 615" fill="none" stroke="#F05E1C" stroke-width="2"/>
      <g transform="translate(600, 337)">
        <rect x="-280" y="-70" width="560" height="140" fill="#111111" stroke="#F05E1C" stroke-width="1.5" rx="4"/>
        <text x="0" y="-20" font-family="'IBM Plex Mono', monospace" font-size="22" font-weight="700" fill="#EDEDED" text-anchor="middle" letter-spacing="2">{icon_symbol} {title_text}</text>
        <text x="0" y="25" font-family="'IBM Plex Mono', monospace" font-size="12" fill="#F05E1C" text-anchor="middle" letter-spacing="2">{subtitle_text}</text>
        <line x1="-240" y1="45" x2="240" y2="45" stroke="#1c1c1c" stroke-width="1"/>
      </g>
      <text x="80" y="90" font-family="'IBM Plex Mono', monospace" font-size="11" fill="#666666" letter-spacing="2">SYS_REF // 0X8F4A</text>
      <text x="1120" y="90" font-family="'IBM Plex Mono', monospace" font-size="11" fill="#F05E1C" text-anchor="end" letter-spacing="2">STATUS: VERIFIED</text>
      <text x="80" y="605" font-family="'IBM Plex Mono', monospace" font-size="11" fill="#666666" letter-spacing="2">LATENCY &lt; 50MS</text>
      <text x="1120" y="605" font-family="'IBM Plex Mono', monospace" font-size="11" fill="#666666" text-anchor="end" letter-spacing="2">HARDWARE IN THE LOOP</text>
    </svg>'''

def make_svg_arch(block1, block2, block3, block4):
    return f'''<svg viewBox="0 0 800 500" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="background:#090909;">
      <defs>
        <pattern id="arch-grid" width="20" height="20" patternUnits="userSpaceOnUse">
          <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#181818" stroke-width="1"/>
        </pattern>
        <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 0 L 10 5 L 0 10 z" fill="#F05E1C"/>
        </marker>
      </defs>
      <rect width="100%" height="100%" fill="url(#arch-grid)"/>
      <text x="40" y="45" font-family="'IBM Plex Mono', monospace" font-size="14" font-weight="600" fill="#F05E1C" letter-spacing="2">SYSTEM ARCHITECTURE &amp; DATA FLOW</text>
      <g transform="translate(60, 180)">
        <rect width="140" height="120" fill="#111" stroke="#333" stroke-width="1.5" rx="4"/>
        <rect width="140" height="4" fill="#F05E1C"/>
        <text x="70" y="45" font-family="'IBM Plex Mono', monospace" font-size="11" font-weight="600" fill="#F05E1C" text-anchor="middle">STAGE 01</text>
        <text x="70" y="75" font-family="'IBM Plex Mono', monospace" font-size="13" font-weight="500" fill="#EDEDED" text-anchor="middle">{block1}</text>
      </g>
      <line x1="200" y1="240" x2="250" y2="240" stroke="#F05E1C" stroke-width="2" marker-end="url(#arrow)"/>
      <g transform="translate(255, 160)">
        <rect width="160" height="160" fill="#141414" stroke="#F05E1C" stroke-width="1.5" rx="4"/>
        <rect width="160" height="6" fill="#F05E1C"/>
        <text x="80" y="40" font-family="'IBM Plex Mono', monospace" font-size="11" font-weight="600" fill="#F05E1C" text-anchor="middle">STAGE 02</text>
        <text x="80" y="75" font-family="'IBM Plex Mono', monospace" font-size="14" font-weight="700" fill="#EDEDED" text-anchor="middle">{block2}</text>
        <text x="80" y="115" font-family="'IBM Plex Mono', monospace" font-size="10" fill="#666" text-anchor="middle">Core Processing</text>
      </g>
      <line x1="415" y1="240" x2="465" y2="240" stroke="#F05E1C" stroke-width="2" marker-end="url(#arrow)"/>
      <g transform="translate(470, 180)">
        <rect width="140" height="120" fill="#111" stroke="#333" stroke-width="1.5" rx="4"/>
        <rect width="140" height="4" fill="#F05E1C"/>
        <text x="70" y="45" font-family="'IBM Plex Mono', monospace" font-size="11" font-weight="600" fill="#F05E1C" text-anchor="middle">STAGE 03</text>
        <text x="70" y="75" font-family="'IBM Plex Mono', monospace" font-size="13" font-weight="500" fill="#EDEDED" text-anchor="middle">{block3}</text>
      </g>
      <line x1="610" y1="240" x2="650" y2="240" stroke="#F05E1C" stroke-width="2" marker-end="url(#arrow)"/>
      <g transform="translate(655, 180)">
        <rect width="105" height="120" fill="#111" stroke="#333" stroke-width="1.5" rx="4"/>
        <rect width="105" height="4" fill="#F05E1C"/>
        <text x="52" y="45" font-family="'IBM Plex Mono', monospace" font-size="10" font-weight="600" fill="#F05E1C" text-anchor="middle">MONITOR</text>
        <text x="52" y="75" font-family="'IBM Plex Mono', monospace" font-size="12" font-weight="500" fill="#EDEDED" text-anchor="middle">{block4}</text>
      </g>
      <path d="M 540 300 L 540 380 L 335 380 L 335 320" fill="none" stroke="#666" stroke-dasharray="4 4" stroke-width="1.5" marker-end="url(#arrow)"/>
      <text x="437" y="400" font-family="'IBM Plex Mono', monospace" font-size="10" fill="#666" text-anchor="middle">Feedback &amp; Telemetry Loop</text>
    </svg>'''

def make_svg_fig2(title_label, subtitle_label):
    return f'''<svg viewBox="0 0 800 500" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="background:#090909;">
      <defs>
        <pattern id="fig-grid" width="20" height="20" patternUnits="userSpaceOnUse">
          <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#161616" stroke-width="1"/>
        </pattern>
      </defs>
      <rect width="100%" height="100%" fill="url(#fig-grid)"/>
      <text x="40" y="45" font-family="'IBM Plex Mono', monospace" font-size="14" font-weight="600" fill="#F05E1C" letter-spacing="2">HARDWARE SCHEMATIC &amp; SIGNAL TIMING</text>
      <g transform="translate(60, 90)">
        <rect width="680" height="340" fill="#0d0d0d" stroke="#222" stroke-width="1.5" rx="4"/>
        <line x1="0" y1="170" x2="680" y2="170" stroke="#333" stroke-width="1" stroke-dasharray="4 4"/>
        <path d="M 40 170 Q 100 50, 160 170 T 280 170 T 400 170 T 520 170 T 640 170" fill="none" stroke="#F05E1C" stroke-width="2.5"/>
        <path d="M 40 250 L 160 250 L 160 110 L 280 110 L 280 250 L 400 250 L 400 110 L 520 110 L 520 250 L 640 250" fill="none" stroke="#666" stroke-width="1.5" stroke-dasharray="2 2"/>
        <circle cx="160" cy="170" r="5" fill="#F05E1C"/>
        <circle cx="280" cy="170" r="5" fill="#F05E1C"/>
        <circle cx="400" cy="170" r="5" fill="#F05E1C"/>
        <text x="50" y="30" font-family="'IBM Plex Mono', monospace" font-size="12" fill="#F05E1C">{title_label}</text>
        <text x="50" y="315" font-family="'IBM Plex Mono', monospace" font-size="11" fill="#666">{subtitle_label}</text>
      </g>
    </svg>'''

def make_gallery_svg(label, num):
    return f'''<svg viewBox="0 0 400 400" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="background:#0c0c0c;">
      <rect width="100%" height="100%" fill="none" stroke="#1c1c1c" stroke-width="2"/>
      <circle cx="200" cy="180" r="70" fill="none" stroke="#F05E1C" stroke-width="1.5" stroke-opacity="0.5"/>
      <circle cx="200" cy="180" r="30" fill="none" stroke="#F05E1C" stroke-width="1"/>
      <line x1="200" y1="80" x2="200" y2="280" stroke="#1c1c1c" stroke-width="1"/>
      <line x1="100" y1="180" x2="300" y2="180" stroke="#1c1c1c" stroke-width="1"/>
      <text x="200" y="320" font-family="'IBM Plex Mono', monospace" font-size="12" font-weight="600" fill="#EDEDED" text-anchor="middle">{label}</text>
      <text x="200" y="345" font-family="'IBM Plex Mono', monospace" font-size="10" fill="#F05E1C" text-anchor="middle" letter-spacing="2">FIGURE 0{num}</text>
    </svg>'''

# 17 Updated Projects Data
projects_data = [
    # 01: Oil Palm Drone
    {
        "slug": "oil-palm-drone",
        "case_num": 1,
        "title": "Autonomous Oil Palm Pollination Drone <span class=\"glow\">·</span> Field-Ready Build",
        "subtitle": "End-to-end autonomous drone for precision agriculture. Core flight control via Pymavlink/MAVSDK with ROS as a validation architecture. Digital twin simulation + SITL/HIL testing, waypoint navigation, real-time YOLOv11 obstacle avoidance, STM32 payload actuation, and a FastAPI web telemetry dashboard.",
        "role": "Embedded System Engineer Intern",
        "client": "PT Syergie Autotek",
        "period": "Jun — Dec 2025",
        "stack_str": "Pixhawk · Jetson · ROS · STM32",
        "metrics": [("92%", "mAP@50 obstacle detection"), ("< 50ms", "control loop latency"), ("100%", "SITL / HIL pass rate")],
        "sections": [("problem", "Problem"), ("approach", "Approach"), ("architecture", "Architecture"), ("firmware", "Firmware & Vision"), ("dashboard", "Dashboard"), ("results", "Results"), ("lessons", "Lessons")],
        "hero_svg": make_svg_cover("AUTONOMOUS POLLINATION DRONE", "PIXHAWK · JETSON NANO · ROS · STM32", "◈"),
        "arch_svg": make_svg_arch("Sensors / Camera", "Jetson Nano + ROS", "STM32 Payload", "FastAPI Ground"),
        "fig2_svg": make_svg_fig2("MAVLink Real-Time Control Loop", "50Hz determinism over serial UART"),
        "gallery_svgs": [make_gallery_svg("YOLO Canopy Vision", 1), make_gallery_svg("FastAPI Dashboard", 2), make_gallery_svg("Field Operation Flight", 3)],
        "stack_chips": ["Pixhawk 2.4.8", "Jetson Nano", "ArduPilot", "ROS Noetic", "MAVSDK / Pymavlink", "YOLOv11", "STM32", "FastAPI", "ReactJS", "SolidWorks", "Gazebo", "SITL / HIL"],
        "body_content": '''
          <h2 id="problem"><span class="num">01</span>Problem</h2>
          <p>Oil palm pollination in Southeast Asian plantations requires manual labor across thousands of hectares during narrow seasonal flowering windows. Worker scarcity and canopy height constraints make manual pollination inefficient and high-risk.</p>
          <p>The objective was to build an autonomous quadrotor UAV capable of navigating low-canopy plantation grids, detecting flower targets with real-time computer vision, and deploying precision powder spray payloads without human pilot intervention.</p>
          <h2 id="approach"><span class="num">02</span>Approach</h2>
          <p>We decoupled system operations into three coupled layers: <em>deterministic flight control</em>, <em>embedded edge vision</em>, and <em>custom payload hardware</em>.</p>
          <ul>
            <li><strong>Flight Stack</strong> — MAVSDK / Pymavlink running on an onboard NVIDIA Jetson Nano, interfacing with ArduPilot on a Pixhawk 2.4.8 flight controller.</li>
            <li><strong>Perception</strong> — Custom YOLOv11 model optimized with TensorRT, running at 30 FPS for obstacle avoidance and flower head identification.</li>
            <li><strong>Payload Board</strong> — Dedicated STM32 MCU managing high-pressure electrostatic spray valves and monitoring tank telemetry via FastAPI WebSockets.</li>
          </ul>
          <div class="figure">
            <div class="frame"><image-slot id="oil-palm-drone-arch" shape="rect" placeholder="System architecture diagram"></image-slot></div>
            <div class="cap"><b>Fig. 01</b> System architecture data flow — flight loop, perception pipeline, and ground control.</div>
          </div>
          <h2 id="architecture"><span class="num">03</span>Architecture</h2>
          <p>Deterministic serial MAVLink protocols handle hard real-time flight navigation while ROS Noetic handles off-board SITL/HIL simulation validation. Keeping ROS off the critical control loop guaranteed zero pub/sub latency spikes in field deployments.</p>
          <h2 id="firmware"><span class="num">04</span>Firmware &amp; Vision</h2>
          <p>The STM32 microcontroller firmware executes a state machine regulating discharge duration and valve safety timeouts:</p>
          <pre><code>// Payload actuation FSM
enum State { IDLE, ARM, DISCHARGE, COOLDOWN };
static State s = IDLE;
void on_telemetry_command(cmd_t c) {
    switch (s) {
        case IDLE:    if (c == ARM_REQ)  s = ARM; break;
        case ARM:     if (c == FIRE)     s = DISCHARGE; break;
        case DISCHARGE: timer_start(150); s = COOLDOWN; break;
        case COOLDOWN:  if (timer_elapsed()) s = IDLE; break;
    }
}</code></pre>
          <div class="figure">
            <div class="frame"><image-slot id="oil-palm-drone-pcb" shape="rect" placeholder="Payload PCB schematic"></image-slot></div>
            <div class="cap"><b>Fig. 02</b> STM32 payload controller schematic and timing validation.</div>
          </div>
          <h2 id="dashboard"><span class="num">05</span>Dashboard</h2>
          <p>A FastAPI telemetry bridge broadcasts GPS position, battery cell voltages, mission status, and live vision inference bounding boxes over WebSockets to a ReactJS ground-station dashboard.</p>
          <div class="gallery">
            <div class="frame"><image-slot id="oil-palm-drone-g1" shape="rect" placeholder="Vision detection"></image-slot></div>
            <div class="frame"><image-slot id="oil-palm-drone-g2" shape="rect" placeholder="Dashboard telemetry"></image-slot></div>
            <div class="frame"><image-slot id="oil-palm-drone-g3" shape="rect" placeholder="Field testing"></image-slot></div>
          </div>
          <h2 id="results"><span class="num">06</span>Results</h2>
          <p>Achieved 92% mAP@50 detection accuracy in field trials, maintaining sub-50ms control loop response and zero crashes across 40+ autonomous test flights.</p>
          <h2 id="lessons"><span class="num">07</span>Lessons</h2>
          <ul>
            <li>Keep critical flight loops deterministic over hardware serial UART.</li>
            <li>Digital twin SITL validation saves weeks of field debugging time.</li>
          </ul>
        '''
    },

    # 02: Rewritten to Adaptive L1 Control on STM32F407
    {
        "slug": "l1-adaptive-control-uav",
        "case_num": 2,
        "title": "HIL Testing Adaptive L1 Control for UAV Heavy Payload Drop <span class=\"glow\">·</span> STM32F407 (Pixhawk)",
        "subtitle": "Implementation and Hardware-in-the-Loop (HIL) validation of an L1 Adaptive Controller for quadrotors facing severe mass drop perturbations and unmodeled environmental disturbances. Carried from SITL in MATLAB to SITL in ROS and HIL on STM32F407 Pixhawk hardware.",
        "role": "Undergraduate Thesis / Research Lead",
        "client": "ITB Control Engineering Lab",
        "period": "Aug 2025 — Present",
        "stack_str": "MATLAB · ROS · C++ · STM32F407 · Pixhawk",
        "metrics": [("L1 Adaptive", "real-time uncertainty estimation"), ("< 0.8s", "payload drop transient recovery"), ("100%", "HIL pass rate on STM32F407")],
        "sections": [("problem", "Problem"), ("math", "L1 Adaptive Math"), ("sitl", "MATLAB to ROS SITL"), ("hil", "STM32F407 HIL Test"), ("results", "Results"), ("lessons", "Lessons")],
        "hero_svg": make_svg_cover("HIL ADAPTIVE L1 UAV CONTROL", "MATLAB · ROS · STM32F407 · PIXHAWK HIL", "◈"),
        "arch_svg": make_svg_arch("Desired Trajectory r(t)", "L1 State Predictor", "L1 Adaptation Law + Filter", "STM32F407 HIL Actuation"),
        "fig2_svg": make_svg_fig2("L1 Adaptive Uncertainty Estimation", "Fast adaptation without high-frequency gain chatter"),
        "gallery_svgs": [make_gallery_svg("MATLAB Trajectory Simulation", 1), make_gallery_svg("ROS Gazebo SITL Twin", 2), make_gallery_svg("STM32F407 Pixhawk HIL", 3)],
        "stack_chips": ["MATLAB", "Simulink", "C++", "STM32F407", "Pixhawk", "ArduPilot", "ROS Noetic", "Gazebo", "SITL / HIL", "L1 Adaptive Control"],
        "body_content": '''
          <h2 id="problem"><span class="num">01</span>Problem</h2>
          <p>When a quadrotor UAV releases a heavy payload mid-flight (up to 40% of total vehicle mass), the sudden mass loss and center-of-gravity displacement induce severe destabilizing torque and altitude drop. Traditional fixed-gain PID or classic adaptive controllers either suffer from slow convergence or high-gain chatter that excites unmodeled structural dynamics.</p>
          <h2 id="math"><span class="num">02</span>L1 Adaptive Math</h2>
          <p>The L1 Adaptive Controller decouples adaptation speed from robustness bounds by inserting a low-pass control filter D(s) after high-gain adaptation. The state predictor and control law equations:</p>
          <pre><code>// L1 Adaptive Control Architecture — C++ implementation outline
// State Predictor: x_hat_dot = Am * x_hat + B * (u + sigma_hat)
Vector3d x_err = x_hat - x_measured;
Vector3d sigma_hat = -inv(B_spec) * (Am * x_err); // Piecewise constant adaptation

// Low-Pass Control Filter (guarantees transient performance & margins)
Vector3d u_adaptive = lowpass_filter.update(-sigma_hat);
Vector3d u_total = u_baseline_pid + u_adaptive;</code></pre>

          <h2 id="sitl"><span class="num">03</span>MATLAB to ROS SITL</h2>
          <p>The controller was first formulated and proven stable in MATLAB / Simulink using Lyapunov functions. The control block was then compiled into C++ nodes for Software-in-the-Loop (SITL) validation in ROS Noetic and Gazebo simulation, subjecting the digital twin quadrotor to random wind gust vectors and instantaneous payload detachment triggers.</p>

          <h2 id="hil"><span class="num">04</span>STM32F407 HIL Test</h2>
          <p>The compiled C++ L1 adaptive module was flashed directly onto an ARM Cortex-M4 STM32F407 microcontroller embedded within a Pixhawk flight controller. In Hardware-in-the-Loop (HIL) mode, the STM32F407 receives real-time flight telemetry from Gazebo over high-speed serial UART and calculates motor PWM outputs at 400Hz.</p>

          <div class="figure">
            <div class="frame"><image-slot id="l1-adaptive-control-uav-arch" shape="rect" placeholder="L1 Adaptive block diagram"></image-slot></div>
            <div class="cap"><b>Fig. 01</b> L1 Adaptive state predictor, adaptation law, and low-pass filter topology.</div>
          </div>

          <h2 id="results"><span class="num">05</span>Results</h2>
          <p>During HIL test payload releases, the L1 adaptive controller reduced altitude drop transient recovery time from 2.6s (baseline PID) to under 0.8s, eliminating motor saturation and chatter while maintaining bounded transient response.</p>

          <h2 id="lessons"><span class="num">06</span>Lessons</h2>
          <ul>
            <li>The low-pass filter in L1 adaptive control allows fast adaptation rates without causing high-frequency actuator oscillations.</li>
            <li>Progressing systematically from MATLAB SITL to ROS SITL to STM32F407 HIL guarantees deployment stability.</li>
          </ul>
        '''
    },

    # 03: TinyML Motor Anomaly
    {
        "slug": "tinyml-motor-anomaly",
        "case_num": 3,
        "title": "TinyML Motor Anomaly Detection <span class=\"glow\">·</span> ESP32-S3 Edge AI",
        "subtitle": "On-device vibration spectrum analysis and autoencoder neural network for industrial motor bearing fault classification. Runs real-time inference on an ESP32-S3 without cloud connectivity.",
        "role": "Firmware & ML Developer",
        "client": "Personal R&D",
        "period": "Oct 2025 — Jan 2026",
        "stack_str": "ESP32-S3 · TensorFlow Lite · C++ · Python",
        "metrics": [("96.4%", "fault classification accuracy"), ("12KB", "model RAM footprint"), ("< 8ms", "on-chip inference latency")],
        "sections": [("problem", "Problem"), ("pipeline", "Feature Pipeline"), ("tinyml", "Model Architecture"), ("hardware", "Hardware & Firmware"), ("results", "Results"), ("lessons", "Lessons")],
        "hero_svg": make_svg_cover("TINYML MOTOR ANOMALY DETECTION", "ESP32-S3 · TENSORFLOW LITE MICRO · C++", "▸"),
        "arch_svg": make_svg_arch("MPU6050 Accelerometer", "FFT & Feature Extract", "ESP32 Autoencoder", "OLED / Local Alert"),
        "fig2_svg": make_svg_fig2("Vibration Frequency Spectrum (FFT)", "Peak harmonic anomalies at bearing fault frequencies"),
        "gallery_svgs": [make_gallery_svg("FFT Spectrum Graph", 1), make_gallery_svg("Autoencoder Tensor", 2), make_gallery_svg("ESP32 Test Setup", 3)],
        "stack_chips": ["TinyML", "TensorFlow Lite Micro", "Python", "C++", "ESP32-S3", "MPU6050", "FFT Analysis", "Edge AI", "FreeRTOS"],
        "body_content": '''
          <h2 id="problem"><span class="num">01</span>Problem</h2>
          <p>Industrial induction motor bearing failures cause costly unscheduled factory downtime. Streaming raw high-frequency vibration data to cloud servers consumes prohibitive network bandwidth.</p>
          <h2 id="pipeline"><span class="num">02</span>Feature Pipeline</h2>
          <p>Vibration signals from an MPU6050 accelerometer are sampled at 1.6 kHz. An onboard 512-point Fast Fourier Transform (FFT) computes spectral energy, crest factor, and kurtosis features locally.</p>
          <h2 id="tinyml"><span class="num">03</span>Model Architecture</h2>
          <p>An Autoencoder Neural Network trained on normal motor operating profiles detects anomalies by calculating reconstruction error (MSE) against incoming spectral vectors.</p>
          <pre><code>// TensorFlow Lite Micro Inference Loop
TfLiteStatus invoke_status = interpreter->Invoke();
if (invoke_status == kTfLiteOk) {
    float mse = calculate_reconstruction_error(input_buf, output_buf, FEATURE_SIZE);
    if (mse > ANOMALY_THRESHOLD) {
        trigger_alarm(FAULT_BEARING_DEGRADATION);
    }
}</code></pre>
          <h2 id="hardware"><span class="num">04</span>Hardware &amp; Firmware</h2>
          <p>Executed on a dual-core ESP32-S3 microcontroller. Core 0 manages 1.6 kHz DMA sensor sampling while Core 1 executes quantized int8 TensorFlow Lite Micro inference in under 8ms.</p>
          <h2 id="results"><span class="num">05</span>Results</h2>
          <p>Achieved 96.4% accuracy in distinguishing normal operation, outer-race bearing defect, and rotor unbalance, using under 12KB of SRAM memory.</p>
          <h2 id="lessons"><span class="num">06</span>Lessons</h2>
          <ul>
            <li>Domain-specific feature engineering (FFT harmonics) drastically reduces neural network size for microcontrollers.</li>
          </ul>
        '''
    },

    # 04: Industrial PID Delivery Box
    {
        "slug": "industrial-pid-delivery-box",
        "case_num": 4,
        "title": "Industrial PID Temperature Food Delivery Box <span class=\"glow\">·</span> Thermal Control",
        "subtitle": "Dual-zone hot and cold climate-controlled food delivery box driven by Peltier thermoelectric coolers, PTC heaters, closed-loop PID control on ESP32 FreeRTOS, and mobile app telemetry.",
        "role": "Embedded & Hardware Engineer",
        "client": "Industrial Product Design",
        "period": "Mar — May 2025",
        "stack_str": "ESP32 · FreeRTOS · PID · Peltier TEC · Kodular",
        "metrics": [("±0.3°C", "temperature stability"), ("23°C / 45°C", "dual hot/cold setpoints"), ("< 12 Min", "transient warm-up time")],
        "sections": [("problem", "Problem"), ("thermal", "Thermal Circuit"), ("pid", "PID Tuning"), ("rtos", "FreeRTOS Tasks"), ("results", "Results"), ("lessons", "Lessons")],
        "hero_svg": make_svg_cover("INDUSTRIAL PID DELIVERY BOX", "ESP32 · FREERTOS · PELTIER TEC · PTC HEATER", "▸"),
        "arch_svg": make_svg_arch("DS18B20 Temp Sensors", "ESP32 PID Controller", "MOSFET H-Bridge Drivers", "Peltier / PTC Thermal"),
        "fig2_svg": make_svg_fig2("PID Closed-Loop Temperature Transient", "Minimal overshoot with steady state error < 0.3°C"),
        "gallery_svgs": [make_gallery_svg("Thermal Chamber CAD", 1), make_gallery_svg("ESP32 Control Board", 2), make_gallery_svg("Kodular App UI", 3)],
        "stack_chips": ["ESP32", "FreeRTOS", "C++", "Arduino", "PID Control", "Peltier TEC", "PTC Heater", "Kodular App", "Hardware Watchdog"],
        "body_content": '''
          <h2 id="problem"><span class="num">01</span>Problem</h2>
          <p>Food delivery services require simultaneous hot (45°C) and cold (23°C) temperature preservation over long urban transit times without exhausting portable battery capacity.</p>
          <h2 id="thermal"><span class="num">02</span>Thermal Circuit</h2>
          <p>Custom insulated dual chamber featuring TEC1-1206 Peltier modules for cooling and PTC ceramic heating elements driven by high-current N-channel MOSFET PWM drivers.</p>
          <h2 id="pid"><span class="num">03</span>PID Tuning</h2>
          <p>Implemented anti-windup discrete PID temperature regulation algorithm in C++:</p>
          <pre><code>// Discrete PID calculation with anti-windup
float error = setpoint - current_temp;
integral += error * dt;
integral = constrain(integral, -MAX_I, MAX_I);
float derivative = (error - prev_error) / dt;
float output = Kp * error + Ki * integral + Kd * derivative;
analogWrite(PWM_PIN, constrain(output, 0, 255));</code></pre>
          <h2 id="rtos"><span class="num">04</span>FreeRTOS Tasks</h2>
          <p>Task 1 handles 10Hz temperature sensor polling and PID loop computation; Task 2 manages OLED display rendering and Bluetooth communication with a custom Kodular mobile app.</p>
          <h2 id="results"><span class="num">05</span>Results</h2>
          <p>Maintained ±0.3°C temperature stability across a 3-hour field test, reaching setpoints within 12 minutes from ambient start.</p>
          <h2 id="lessons"><span class="num">06</span>Lessons</h2>
          <ul>
            <li>Thermal mass modeling is vital to prevent PWM overshoot in thermoelectric cooling systems.</li>
          </ul>
        '''
    },

    # 05: Custom Mini STM32 PCB
    {
        "slug": "custom-stm32-pcb",
        "case_num": 5,
        "title": "Custom Mini STM32 PCB <span class=\"glow\">·</span> KiCad 2-Layer Layout",
        "subtitle": "Complete design lifecycle of an ARM Cortex-M3 (STM32F103C8T6) development board in KiCad. Includes LDO regulator power stage, 16MHz crystal load cap calculations, USB 2.0 differential routing, and ground plane shielding.",
        "role": "PCB Design Engineer",
        "client": "Personal Hardware Project",
        "period": "Jan 2025",
        "stack_str": "KiCad 8.0 · STM32F103 · PCB Layout · EMC",
        "metrics": [("2-Layer", "impedance-controlled PCB"), ("16 MHz", "crystal load cap precision"), ("0 EMI", "clean ground plane shielding")],
        "sections": [("schematic", "Schematic Design"), ("power", "Power & Crystal"), ("layout", "PCB Layout & Traces"), ("gerber", "Gerber Pre-flight"), ("results", "Results"), ("lessons", "Lessons")],
        "hero_svg": make_svg_cover("CUSTOM MINI STM32 PCB", "KICAD 8.0 · STM32F103C8T6 · 2-LAYER LAYOUT", "▸"),
        "arch_svg": make_svg_arch("USB 5V Supply", "AMS1117-3.3 LDO", "STM32 MCU Core", "SWD Debug / GPIO"),
        "fig2_svg": make_svg_fig2("USB 2.0 Differential Pair Routing", "90 Ohm differential impedance matched trace geometry"),
        "gallery_svgs": [make_gallery_svg("KiCad Schematic", 1), make_gallery_svg("PCB Traces 2-Layer", 2), make_gallery_svg("3D PCB Render", 3)],
        "stack_chips": ["KiCad 8.0", "STM32F103C8T6", "PCB Design", "Signal Integrity", "EMC / EMI", "SWD Debug", "Gerber Generation"],
        "body_content": '''
          <h2 id="schematic"><span class="num">01</span>Schematic Design</h2>
          <p>Created full schematic in KiCad 8.0 for STM32F103C8T6 ARM Cortex-M3 core, decoupling capacitors per power pin pair, NRST reset circuit, and BOOT0 selection jumpers.</p>
          <h2 id="power"><span class="num">02</span>Power &amp; Crystal</h2>
          <p>AMS1117 3.3V linear regulator steps down USB 5V supply with low-ESR tantalum input/output caps. Calculated 16MHz high-speed crystal load capacitors using formula:</p>
          <pre><code>// Crystal Load Capacitance Formula
C_L = 16pF, C_stray = 3pF
C1 = C2 = 2 * (C_L - C_stray) = 2 * (16 - 3) = 26pF (selected 22pF standard)</code></pre>
          <h2 id="layout"><span class="num">03</span>PCB Layout &amp; Traces</h2>
          <p>2-layer 1.6mm FR4 PCB layout. Designed continuous bottom layer ground plane for low impedance return paths. Routed USB D+/D- as 90Ω differential pairs with matched trace lengths.</p>
          <h2 id="gerber"><span class="num">04</span>Gerber Pre-flight</h2>
          <p>Ran KiCad DRC checks for minimum trace width (0.2mm), clear vias, silk screen overlaps, and solder mask expansion before exporting Gerber and NC Drill manufacturing files.</p>
          <h2 id="results"><span class="num">05</span>Results</h2>
          <p>Fabricated boards booted cleanly on first power-up, establishing SWD debugging connection in STM32CubeIDE and maintaining stable 16MHz system clocking.</p>
          <h2 id="lessons"><span class="num">06</span>Lessons</h2>
          <ul>
            <li>Decoupling capacitors must be placed immediately adjacent to MCU VDD pins to minimize parasitic inductance.</li>
          </ul>
        '''
    },

    # 06: Intelligent EV Charging Station
    {
        "slug": "intelligent-ev-charging-station",
        "case_num": 6,
        "title": "Intelligent EV Charging Station <span class=\"glow\">·</span> CSMS & Grid AI",
        "subtitle": "Full-stack Charging Station Management System (CSMS) featuring FastAPI backend, XGBoost grid demand forecasting, ReactJS analytics dashboard, and Raspberry Pi edge kiosks with RFID authentication.",
        "role": "Transport Technology Intern",
        "client": "PT Rekacipta Inovasi ITB",
        "period": "Feb — Jul 2026",
        "stack_str": "ReactJS · FastAPI · XGBoost · Raspberry Pi · RFID",
        "metrics": [("98.1%", "grid load forecast accuracy"), ("150ms", "RFID authorization latency"), ("2 EV Models", "homologation compliance")],
        "sections": [("problem", "Problem"), ("backend", "FastAPI & XGBoost"), ("kiosk", "Edge Kiosk & RFID"), ("homologation", "EV Homologation"), ("results", "Results"), ("lessons", "Lessons")],
        "hero_svg": make_svg_cover("INTELLIGENT EV CHARGING STATION", "FASTAPI · REACTJS · XGBOOST · RASPBERRY PI", "▸"),
        "arch_svg": make_svg_arch("PN532 RFID Kiosk", "Raspberry Pi Edge", "FastAPI CSMS Core", "XGBoost Grid AI"),
        "fig2_svg": make_svg_fig2("Grid Demand Prediction Curve", "XGBoost forecasted peak vs actual load profile"),
        "gallery_svgs": [make_gallery_svg("CSMS Dashboard UI", 1), make_gallery_svg("RFID Kiosk Station", 2), make_gallery_svg("XGBoost Load Model", 3)],
        "stack_chips": ["ReactJS", "FastAPI", "XGBoost", "Raspberry Pi", "MySQL", "PN532 RFID", "MQTT", "Python", "EV Homologation"],
        "body_content": '''
          <h2 id="problem"><span class="num">01</span>Problem</h2>
          <p>Rapid adoption of electric two-wheelers and light EVs strains local distribution transformers during peak hours. Charging networks require intelligent load balancing and secure RFID user management.</p>
          <h2 id="backend"><span class="num">02</span>FastAPI &amp; XGBoost</h2>
          <p>Developed a asynchronous FastAPI CSMS backend that uses an XGBoost machine learning model to predict grid load 24 hours in advance, dynamically capping maximum charging current during grid peak hours.</p>
          <h2 id="kiosk"><span class="num">03</span>Edge Kiosk &amp; RFID</h2>
          <p>Raspberry Pi edge controller interfaces with a PN532 RFID reader via I2C for fast user authentication (<150ms) and drives relays via Modbus RTU.</p>
          <h2 id="homologation"><span class="num">04</span>EV Homologation</h2>
          <p>Assisted in the regulatory homologation process for 2 EV prototype vehicles, verifying electrical safety, wiring insulation standards, and battery management integration with government regulators.</p>
          <h2 id="results"><span class="num">05</span>Results</h2>
          <p>Achieved 98.1% demand forecasting accuracy, preventing transformer overload during concurrent vehicle charging tests.</p>
          <h2 id="lessons"><span class="num">06</span>Lessons</h2>
          <ul>
            <li>Asynchronous Python backends combined with WebSockets deliver smooth real-time telemetry rendering.</li>
          </ul>
        '''
    },

    # 07: IIoT Capstone Motor Control
    {
        "slug": "iiot-motor-control-system",
        "case_num": 7,
        "title": "IIoT Capstone — Motor Control System <span class=\"glow\">·</span> SCADA & HMI",
        "subtitle": "Multi-tier industrial automation architecture integrating Omron PLCs over Modbus RS485, local Weintek touch HMIs, Node-RED MQTT gateway, and cloud NextJS dashboard backed by MongoDB.",
        "role": "Systems & Automation Lead",
        "client": "Engineering Physics Capstone",
        "period": "Sep — Dec 2024",
        "stack_str": "Node-RED · NextJS · MongoDB · Omron PLC · Weintek",
        "metrics": [("100ms", "SCADA refresh interval"), ("99.9%", "data acquisition uptime"), ("2-Tier", "HMI & Cloud redundancy")],
        "sections": [("problem", "Problem"), ("plc", "PLC & Modbus"), ("hmi", "Weintek HMI"), ("cloud", "NextJS & MongoDB"), ("results", "Results"), ("lessons", "Lessons")],
        "hero_svg": make_svg_cover("IIOT CAPSTONE MOTOR CONTROL", "OMRON PLC · WEINTEK HMI · NODE-RED · NEXTJS", "▸"),
        "arch_svg": make_svg_arch("Omron PLC / RS485", "Weintek Local HMI", "Node-RED Gateway", "NextJS Cloud DB"),
        "fig2_svg": make_svg_fig2("Modbus RS485 Register Polling", "Deterministic 100ms register sync across 8 motor nodes"),
        "gallery_svgs": [make_gallery_svg("Weintek Screen UI", 1), make_gallery_svg("Node-RED Flow", 2), make_gallery_svg("NextJS Analytics", 3)],
        "stack_chips": ["Node-RED", "NextJS", "MongoDB", "Weintek HMI", "MQTT", "Omron PLC", "CX Designer", "Modbus RS485"],
        "body_content": '''
          <h2 id="problem"><span class="num">01</span>Problem</h2>
          <p>Industrial motor control centers require low-latency local operator touchscreens combined with cloud-based remote condition monitoring and historical fault logging.</p>
          <h2 id="plc"><span class="num">02</span>PLC &amp; Modbus</h2>
          <p>Programmed Omron CP1E PLCs using CX-Programmer ladder logic for motor contactor interlocks, overload protection, and Modbus RS485 communication at 19200 baud.</p>
          <h2 id="hmi"><span class="num">03</span>Weintek HMI</h2>
          <p>Configured Weintek touch HMI displays using EasyBuilder Pro for real-time motor start/stop control, current draw gauges, and local alarm acknowledgement.</p>
          <h2 id="cloud"><span class="num">04</span>NextJS &amp; MongoDB</h2>
          <p>A Node-RED industrial gateway translates Modbus registers into JSON MQTT payloads sent to a NextJS web application with MongoDB time-series storage.</p>
          <h2 id="results"><span class="num">05</span>Results</h2>
          <p>Maintained 100ms local SCADA refresh rates and zero data loss over a continuous 72-hour stress test.</p>
          <h2 id="lessons"><span class="num">06</span>Lessons</h2>
          <ul>
            <li>Isolating local industrial HMI control from cloud network traffic ensures factory floor safety even during internet outages.</li>
          </ul>
        '''
    },

    # 08: Micro HydroPower HMI
    {
        "slug": "micro-hydro-hmi-system",
        "case_num": 8,
        "title": "Micro HydroPower HMI Learning System <span class=\"glow\">·</span> ISA101 SCADA",
        "subtitle": "Ergonomic industrial human-machine interface for village-scale micro-hydro generation plants, built to ISA101 and ISO 11064-5 standards with FreeRTOS DAQ and MySQL trend logging.",
        "role": "Industrial Automation Lead",
        "client": "Renewable Energy Lab",
        "period": "Oct — Dec 2024",
        "stack_str": "Node-RED · MQTT · MySQL · RTOS · ISA101",
        "metrics": [("ISA101", "ergonomic SCADA standard"), ("50ms", "fault trip detection"), ("100%", "role-based access control")],
        "sections": [("problem", "Problem"), ("isa101", "ISA101 HMI Standard"), ("daq", "FreeRTOS DAQ"), ("database", "MySQL Logging"), ("results", "Results"), ("lessons", "Lessons")],
        "hero_svg": make_svg_cover("MICRO HYDROPOWER HMI SYSTEM", "NODE-RED · ISA101 STANDARD · MYSQL · FREERTOS", "▸"),
        "arch_svg": make_svg_arch("Turbine Flow & Pressure", "FreeRTOS Sensor Node", "Node-RED ISA101 HMI", "MySQL Trend Logger"),
        "fig2_svg": make_svg_fig2("High-Performance Ergonomic Gray Scale", "Dark gray background reduces operator eye fatigue"),
        "gallery_svgs": [make_gallery_svg("ISA101 HMI Screen", 1), make_gallery_svg("Turbine Mimic Map", 2), make_gallery_svg("MySQL Trend Plot", 3)],
        "stack_chips": ["Node-RED", "MQTT", "MySQL", "FreeRTOS", "ISA101 Standard", "ISO 11064-5", "Industrial SCADA"],
        "body_content": '''
          <h2 id="problem"><span class="num">01</span>Problem</h2>
          <p>Remote micro-hydro power stations in rural regions suffer from complex, cluttered operator graphics that hide critical alarm conditions and increase human error during grid synchronization.</p>
          <h2 id="isa101"><span class="num">02</span>ISA101 HMI Standard</h2>
          <p>Designed a high-performance SCADA visual layout following ISA101 standards: high-contrast muted grays for normal operation, reserving bright red/amber colors strictly for active safety alarms.</p>
          <h2 id="daq"><span class="num">03</span>FreeRTOS DAQ</h2>
          <p>Microcontroller sensor nodes running FreeRTOS acquire turbine RPM, water head pressure, generator voltage, and grid frequency at 20Hz.</p>
          <h2 id="database"><span class="num">04</span>MySQL Logging</h2>
          <p>All process variables and operator actions are archived into MySQL database tables, enabling automated weekly generation throughput reports.</p>
          <h2 id="results"><span class="num">05</span>Results</h2>
          <p>Operator response time to simulated overspeed faults improved by 64% compared to legacy colorful 2D SCADA displays.</p>
          <h2 id="lessons"><span class="num">06</span>Lessons</h2>
          <ul>
            <li>Muted, gray-scale HMI visuals significantly enhance situational awareness in critical power control rooms.</li>
          </ul>
        '''
    },

    # 09: SAP Flow Sensor
    {
        "slug": "sap-flow-sensor",
        "case_num": 9,
        "title": "Plant SAP Flow Sensor <span class=\"glow\">·</span> Precision Analog DAQ",
        "subtitle": "Compact plant water transportation monitor utilizing the Heat-Ratio Method (HRM), low-noise instrumentation op-amps, differential thermocouple DAQ, and custom 3D-printed SLA enclosure.",
        "role": "Analog & Embedded Developer",
        "client": "Precision Agriculture Lab",
        "period": "Apr — Jun 2024",
        "stack_str": "Analog Circuit · Thermocouple · 3D Design",
        "metrics": [("0.05°C", "differential temperature precision"), ("< 2.5W", "probe heat pulse energy"), ("100%", "weatherproof SLA enclosure")],
        "sections": [("problem", "Problem"), ("hrm", "Heat-Ratio Method"), ("analog", "Analog Front End"), ("enclosure", "3D CAD Enclosure"), ("results", "Results"), ("lessons", "Lessons")],
        "hero_svg": make_svg_cover("PLANT SAP FLOW SENSOR", "INSTRUMENTATION OP-AMP · THERMOCOUPLE · 3D CAD", "▸"),
        "arch_svg": make_svg_arch("Heat-Pulse Probe", "Op-Amp Instrumentation", "ADC 16-Bit Sampler", "Plant Health Log"),
        "fig2_svg": make_svg_fig2("Differential Temperature Heat Pulse Curve", "Upstream vs downstream thermal dissipation curve"),
        "gallery_svgs": [make_gallery_svg("Op-Amp Schematic", 1), make_gallery_svg("3D Printed Probe", 2), make_gallery_svg("Sap Flow Plot", 3)],
        "stack_chips": ["Analog Circuit Design", "Thermocouples", "Instrumentation Amplifiers", "SolidWorks", "3D Printing", "C++", "Signal Processing"],
        "body_content": '''
          <h2 id="problem"><span class="num">01</span>Problem</h2>
          <p>Monitoring plant sap flow (water transpiration rate) in agricultural crops requires non-destructive micro-temperature sensing inside stem tissue without disrupting sap xylem pathways.</p>
          <h2 id="hrm"><span class="num">02</span>Heat-Ratio Method</h2>
          <p>Implemented the Heat-Ratio Method (HRM): a short 2-second heat pulse is injected into the stem, and differential temperature ratio between equidistant upstream and downstream probes measures velocity.</p>
          <h2 id="analog"><span class="num">03</span>Analog Front End</h2>
          <p>Designed a low-noise instrumentation amplifier circuit capable of resolving microvolt T-type thermocouple differential voltages corresponding to 0.05°C temperature resolution.</p>
          <h2 id="enclosure"><span class="num">04</span>3D CAD Enclosure</h2>
          <p>Modeled a SLA 3D-printed IP65 weatherproof probe housing in SolidWorks, ensuring thermal isolation between the heating element and sensitive electronics.</p>
          <h2 id="results"><span class="num">05</span>Results</h2>
          <p>Successfully logged diurnal plant transpiration dynamics across 14-day field deployments, matching reference gravimetric water loss data.</p>
          <h2 id="lessons"><span class="num">06</span>Lessons</h2>
          <ul>
            <li>High-gain differential instrumentation circuits require careful ground guard shielding against EMI.</li>
          </ul>
        '''
    },

    # 10: Soccer Robot EP Lab
    {
        "slug": "soccer-robot-ep-lab",
        "case_num": 10,
        "title": "Soccer Robot — Engineering Physics Lab <span class=\"glow\">·</span> Holonomic Drive",
        "subtitle": "3D-modeled mobile robot with 3-wheel omnidirectional holonomic kinematics, custom Android control app written in Kotlin, Arduino C++ firmware, and WiFi UDP control loop.",
        "role": "Mechanical Crew & Team Lead",
        "client": "ITB Robotics Unit (URO) / Lab II",
        "period": "Sep 2023 — Jan 2025",
        "stack_str": "Arduino · C++ · Android Studio · Kotlin · SolidWorks",
        "metrics": [("1.8 m/s", "omni-directional speed"), ("< 20ms", "wireless UDP latency"), ("3-Wheel", "holonomic kinematics")],
        "sections": [("problem", "Problem"), ("kinematics", "Holonomic Math"), ("mechanical", "SolidWorks Design"), ("android", "Android App"), ("results", "Results"), ("lessons", "Lessons")],
        "hero_svg": make_svg_cover("SOCCER ROBOT OMNI DRIVE", "ARDUINO · KOTLIN · SOLIDWORKS · HOLONOMIC CAD", "▸"),
        "arch_svg": make_svg_arch("Android App Joystick", "WiFi UDP Socket", "Arduino Controller", "3 Omni-Wheel Motors"),
        "fig2_svg": make_svg_fig2("Holonomic Kinematic Velocity Vector Matrix", "3-Wheel omni matrix mapping Vx, Vy, W to motor PWM"),
        "gallery_svgs": [make_gallery_svg("SolidWorks 3D Model", 1), make_gallery_svg("Android Kotlin App", 2), make_gallery_svg("Field Competition", 3)],
        "stack_chips": ["Arduino", "C++", "Android Studio", "Kotlin", "SolidWorks", "3D Printing", "WiFi UDP", "Kinematics"],
        "body_content": '''
          <h2 id="problem"><span class="num">01</span>Problem</h2>
          <p>Robotic soccer competitions demand rapid multi-directional maneuvering and instantaneous vector rotation without stopping to turn.</p>
          <h2 id="kinematics"><span class="num">02</span>Holonomic Math</h2>
          <p>Implemented 3-wheel omnidirectional drive kinematics converting target velocity vectors (Vx, Vy, ω) into individual motor PWM speeds:</p>
          <pre><code>// 3-Wheel Holonomic Matrix Transformation
v1 = -sin(theta)*Vx + cos(theta)*Vy + R*omega;
v2 = -sin(theta+120°)*Vx + cos(theta+120°)*Vy + R*omega;
v3 = -sin(theta+240°)*Vx + cos(theta+240°)*Vy + R*omega;</code></pre>
          <h2 id="mechanical"><span class="num">03</span>SolidWorks Design</h2>
          <p>Designed a lightweight 3D-printed chassis housing 12V high-torque DC gearmotors, custom omni-wheels, motor driver bridge PCBs, and LiPo battery pack.</p>
          <h2 id="android"><span class="num">04</span>Android App</h2>
          <p>Built a custom touch joystick remote application in Android Studio (Kotlin) transmitting low-latency UDP control packets over local WiFi.</p>
          <h2 id="results"><span class="num">05</span>Results</h2>
          <p>Achieved 1.8 m/s maximum sprint velocity and under 20ms wireless command latency during lab testing.</p>
          <h2 id="lessons"><span class="num">06</span>Lessons</h2>
          <ul>
            <li>Omnidirectional wheels require precise weight distribution to prevent wheel slippage on slippery field surfaces.</li>
          </ul>
        '''
    },

    # 11: New Project — PCB Reflow Conveyor with CV Defect Sorting
    {
        "slug": "pcb-reflow-conveyor-cv-sorting",
        "case_num": 11,
        "title": "PCB Reflow Heating Conveyor with CV Defect Sorting <span class=\"glow\">·</span> Smart Assembly",
        "subtitle": "Industrial-grade automated PCB reflow soldering conveyor system featuring closed-loop PID thermal profile control, stepper-driven conveyor bed, and an embedded OpenCV computer vision inspection node for real-time solder bridge, tombstoning, and component alignment defect sorting.",
        "role": "Embedded & Automation Lead",
        "client": "Manufacturing Automation Lab",
        "period": "Oct — Dec 2025",
        "stack_str": "OpenCV · Python · STM32 · PID Thermal · Stepper Motor",
        "metrics": [("±1.5°C", "reflow thermal profile precision"), ("95.8%", "CV defect sorting accuracy"), ("120 PCB/hr", "conveyor throughput")],
        "sections": [("problem", "Problem"), ("thermal", "PID Reflow Profile"), ("conveyor", "Stepper Conveyor Bed"), ("vision", "OpenCV Inspection"), ("results", "Results"), ("lessons", "Lessons")],
        "hero_svg": make_svg_cover("PCB REFLOW CONVEYOR WITH CV SORTING", "OPENCV · STM32 · PID THERMAL · STEPPER DRIVE", "∷"),
        "arch_svg": make_svg_arch("PCB Conveyor Bed", "PID Thermal Tunnel", "OpenCV Vision Camera", "Pneumatic Defect Sorter"),
        "fig2_svg": make_svg_fig2("Standard Lead-Free Reflow Profile Curve", "Preheat (150°C), Soak, Reflow (245°C peak), and Cooling zones"),
        "gallery_svgs": [make_gallery_svg("Reflow Tunnel CAD", 1), make_gallery_svg("OpenCV Bounding Box UI", 2), make_gallery_svg("Conveyor Control PCB", 3)],
        "stack_chips": ["OpenCV", "Python", "STM32", "PID Thermal Control", "Stepper Motors", "SolidWorks", "Computer Vision", "Industrial Automation"],
        "body_content": '''
          <h2 id="problem"><span class="num">01</span>Problem</h2>
          <p>Manual PCB prototype reflow soldering leads to uneven heating and defects such as solder bridging, tombstoning (component lifting), and misaligned SMD packages. Traditional automated SMT inspection lines are cost-prohibitive for small-scale R&D electronics labs.</p>

          <h2 id="thermal"><span class="num">02</span>PID Reflow Profile</h2>
          <p>Designed a multi-zone infrared heating tunnel regulated by an STM32 microcontroller executing closed-loop PID control over SSR relays. The system dynamically follows standard SAC305 lead-free reflow profile curves (preheat 150°C, soak 180°C, peak reflow 245°C, and active fan cooling).</p>
          <pre><code>// Thermal Reflow Profile State Machine
enum ReflowStage { PREHEAT, SOAK, REFLOW_PEAK, COOLING };
void update_reflow_profile(float current_temp, float elapsed_sec) {
    float target_setpoint = calculate_profile_target(elapsed_sec);
    float pwm_out = pid_compute(target_setpoint, current_temp);
    set_ssr_heating_power(pwm_out);
}</code></pre>

          <h2 id="conveyor"><span class="num">03</span>Stepper Conveyor Bed</h2>
          <p>Engineered a stainless steel mesh conveyor belt driven by a high-torque NEMA17 stepper motor. The speed profile is dynamically synchronized with the heating zone timers to ensure uniform dwell time in each thermal stage.</p>

          <h2 id="vision"><span class="num">04</span>OpenCV Inspection</h2>
          <p>Positioned an overhead camera at the conveyor exit. An onboard Raspberry Pi / Python node executing OpenCV algorithms performs template matching, edge detection, and contour analysis to detect solder bridges, tombstoned resistors, and misplaced ICs, activating a pneumatic arm to eject defective boards.</p>

          <div class="figure">
            <div class="frame"><image-slot id="pcb-reflow-conveyor-cv-sorting-arch" shape="rect" placeholder="Reflow Conveyor System Diagram"></image-slot></div>
            <div class="cap"><b>Fig. 01</b> Integrated thermal reflow tunnel, stepper transport, and OpenCV vision inspection pipeline.</div>
          </div>

          <h2 id="results"><span class="num">05</span>Results</h2>
          <p>Achieved ±1.5°C thermal tracking accuracy across the 245°C reflow curve and 95.8% accuracy in identifying SMD soldering defects at a processing speed of 120 PCBs per hour.</p>

          <h2 id="lessons"><span class="num">06</span>Lessons</h2>
          <ul>
            <li>Diffuse ring lighting is crucial above the vision camera to eliminate solder joint glare during automated optical inspection (AOI).</li>
          </ul>
        '''
    },

    # 12: New Project — Hourglass PCB with ATmega328P
    {
        "slug": "hourglass-atmega328p-pcb",
        "case_num": 12,
        "title": "Hourglass PCB with ATmega328P <span class=\"glow\">·</span> Electronic Sand Physics",
        "subtitle": "An aesthetic electronic sand hourglass PCB featuring an array of 60 SMD LEDs arranged in an hourglass contour, driven by an ATmega328P microcontroller with an MPU6050 accelerometer for tilt sensing and real-time gravity physics simulation.",
        "role": "Hardware & Firmware Designer",
        "client": "Personal Hardware Project",
        "period": "Jul — Aug 2025",
        "stack_str": "ATmega328P · KiCad 8.0 · MPU6050 · C++",
        "metrics": [("60 SMD LEDs", "matrix sand display"), ("< 2mA", "deep sleep power current"), ("60 Hz", "gravity physics loop")],
        "sections": [("concept", "Concept & Hardware"), ("schematic", "KiCad PCB Design"), ("physics", "Digital Gravity Physics"), ("power", "Low-Power Firmware"), ("results", "Results"), ("lessons", "Lessons")],
        "hero_svg": make_svg_cover("HOURGLASS ATMEGA328P PCB", "KICAD 8.0 · ATMEGA328P · MPU6050 · SMD LED MATRIX", "⏳"),
        "arch_svg": make_svg_arch("MPU6050 Tilt Sensor", "ATmega328P Core", "LED Matrix Drivers", "60 SMD LED Hourglass Display"),
        "fig2_svg": make_svg_fig2("Digital Sand Falling State Vector", "Grid cellular automata mapping gravity vector to LED pixel move"),
        "gallery_svgs": [make_gallery_svg("KiCad Hourglass Outline", 1), make_gallery_svg("SMD LED Trace Routing", 2), make_gallery_svg("Physical PCB Sand Flow", 3)],
        "stack_chips": ["ATmega328P", "KiCad 8.0", "MPU6050", "C++", "LED Matrix", "Cellular Automata", "Low Power Firmware"],
        "body_content": '''
          <h2 id="concept"><span class="num">01</span>Concept &amp; Hardware</h2>
          <p>Designed a decorative, interactive electronic hourglass PCB. An array of 60 SMD 0805 LEDs arranged in two symmetrical funnel chambers simulates falling grains of sand when the board is held upright, tilted, or flipped upside down.</p>

          <h2 id="schematic"><span class="num">02</span>KiCad PCB Design</h2>
          <p>Created a custom hourglass-contoured PCB outline in KiCad 8.0. The ATmega328P microcontroller drives the 60 LEDs via Charlieplexed matrix switching, minimizing required GPIO pins while maintaining bright, uniform illumination.</p>

          <h2 id="physics"><span class="num">03</span>Digital Gravity Physics</h2>
          <p>An MPU6050 6-axis accelerometer measures tilt angles over I2C at 60 Hz. A cellular automata gravity algorithm computes sand grain displacements, causing LED "grains" to trickle through the narrow neck into the bottom chamber under simulated acceleration vectors.</p>
          <pre><code>// Gravity cellular automata pixel movement
void update_sand_physics(float ax, float ay) {
    for (int y = MATRIX_HEIGHT - 1; y >= 0; y--) {
        for (int x = 0; x < MATRIX_WIDTH; x++) {
            if (grid[x][y] == SAND_PARTICLE) {
                if (can_move_down(x, y, ax, ay)) move_particle(x, y, DOWN);
                else if (can_move_diag(x, y, ax, ay)) move_particle(x, y, DIAG);
            }
        }
    }
}</code></pre>

          <h2 id="power"><span class="num">04</span>Low-Power Firmware</h2>
          <p>When left stationary on a flat surface for over 30 seconds, the ATmega328P enters deep sleep mode with pin-change interrupts enabled on the MPU6050 interrupt line, dropping power consumption below 2mA.</p>

          <h2 id="results"><span class="num">05</span>Results</h2>
          <p>Delivered an intuitive, highly responsive electronic hourglass with smooth 60 FPS sand animation and seamless flip detection.</p>

          <h2 id="lessons"><span class="num">06</span>Lessons</h2>
          <ul>
            <li>Charlieplexing LED arrays dramatically reduces pin count, but requires precise duty cycle timing to prevent flickering.</li>
          </ul>
        '''
    },

    # 13: New Project — Mini Logic Analyzer
    {
        "slug": "mini-logic-analyzer",
        "case_num": 13,
        "title": "Mini Logic Analyzer <span class=\"glow\">·</span> 8-Channel 24MHz DAQ",
        "subtitle": "Compact, high-speed 8-channel digital logic analyzer built with STM32 microcontroller DMA input capture, sampling logic signals up to 24 MHz, and streaming real-time protocol analysis (UART, SPI, I2C) to a desktop GUI.",
        "role": "Firmware & Instrumentation Lead",
        "client": "Personal Instrument Project",
        "period": "Nov 2025 — Jan 2026",
        "stack_str": "STM32F4 · C++ · Fast DMA · Protocol Decoder",
        "metrics": [("24 MHz", "max digital sampling rate"), ("8 Channels", "parallel input capture"), ("< 1μs", "hardware trigger resolution")],
        "sections": [("problem", "Problem"), ("dma", "STM32 Timer DMA DAQ"), ("trigger", "Hardware Triggers"), ("decoders", "Protocol Decoders"), ("results", "Results"), ("lessons", "Lessons")],
        "hero_svg": make_svg_cover("MINI LOGIC ANALYZER", "STM32F4 · 24MHZ DMA CAPTURE · 8-CHANNEL SPI/I2C", "⚡"),
        "arch_svg": make_svg_arch("8-Ch Digital Probe", "STM32F4 GPIO Port + DMA", "Circular Buffer RAM", "USB High-Speed GUI"),
        "fig2_svg": make_svg_fig2("8-Channel Logic Waveform Timing Trace", "Synchronous UART TX/RX and SPI CLK/MOSI/MISO trace"),
        "gallery_svgs": [make_gallery_svg("Logic Analyzer Enclosure", 1), make_gallery_svg("SPI Decoder GUI", 2), make_gallery_svg("Signal Capture Waveform", 3)],
        "stack_chips": ["STM32F4", "C++", "DMA Sampling", "Signal Processing", "UART Decoder", "SPI Decoder", "I2C Decoder", "USB HID"],
        "body_content": '''
          <h2 id="problem"><span class="num">01</span>Problem</h2>
          <p>Debugging low-level embedded bus communications (SPI, I2C, UART) during firmware development requires high-speed digital signal acquisition. Commercial benchtop logic analyzers are bulky and expensive for portable bench field work.</p>

          <h2 id="dma"><span class="num">02</span>STM32 Timer DMA DAQ</h2>
          <p>Built an 8-channel logic capture instrument on an ARM Cortex-M4 STM32F4 microcontroller. Configured GPIO Port A parallel inputs triggered by Timer 1 DMA requests, streaming 8-bit digital logic snapshots directly into a circular SRAM buffer at up to 24 MHz sampling frequency without CPU overhead.</p>
          <pre><code>// STM32 Timer DMA GPIO Sampling Configuration
void init_logic_dma_capture(uint8_t* buffer, uint32_t length) {
    DMA_Config(DMA1_Stream5, (uint32_t)&(GPIOA->IDR), (uint32_t)buffer, length);
    TIM_Enable_DMA_Request(TIM1);
    TIM_Start(TIM1); // Triggers 24MHz parallel byte reads
}</code></pre>

          <h2 id="trigger"><span class="num">03</span>Hardware Triggers</h2>
          <p>Implemented configurable pre-trigger and post-trigger memory buffers with rising edge, falling edge, and high/low level pattern matching trigger conditions with sub-microsecond response.</p>

          <h2 id="decoders"><span class="num">04</span>Protocol Decoders</h2>
          <p>Engineered desktop host software in C++ that parses raw logic frame streams and executes real-time protocol decoding for UART baud rates, SPI data bytes, and I2C ACK/NACK framing.</p>

          <h2 id="results"><span class="num">05</span>Results</h2>
          <p>Successfully captured and decoded 12 MHz SPI bus traffic and 115200 baud UART communications with clean 8-channel waveform alignment.</p>

          <h2 id="lessons"><span class="num">06</span>Lessons</h2>
          <ul>
            <li>Utilizing hardware DMA transfers directly from MCU GPIO input registers is key to achieving multi-megahertz digital sampling.</li>
          </ul>
        '''
    },

    # 14: Batik Coagulant Modular Unit
    {
        "slug": "batik-coagulant-unit",
        "case_num": 14,
        "title": "Batik Wastewater Coagulant Modular Unit <span class=\"glow\">·</span> Eco Tech",
        "subtitle": "Modular, low-cost wastewater treatment reactor for artisanal batik cottage industries, implementing chemical coagulation, natural bio-flocculant mixing, and gravimetric sludge settling.",
        "role": "Mechanical Design Engineer",
        "client": "Appropriate Tech Project",
        "period": "Aug 2024",
        "stack_str": "SolidWorks · CAD · Fluid Dynamics · Environmental",
        "metrics": [("500 L/hr", "treatment flow rate"), ("92%", "dye flocculation efficiency"), ("3-Stage", "settling & filtration grid")],
        "sections": [("problem", "Problem"), ("cad", "SolidWorks 3D Model"), ("mixing", "Flocculation Fluidics"), ("results", "Results"), ("lessons", "Lessons")],
        "hero_svg": make_svg_cover("BATIK WASTEWATER COAGULANT UNIT", "SOLIDWORKS · FLUID DYNAMICS · ECO-ENGINEERING", "⊕"),
        "arch_svg": make_svg_arch("Batik Dye Input", "Rapid Coagulation Mixer", "Slow Flocculation Tank", "Clean Water Discharge"),
        "fig2_svg": make_svg_fig2("Gravimetric Sludge Settling Velocity", "Stokes settling velocity profile in 3-stage baffle chamber"),
        "gallery_svgs": [make_gallery_svg("SolidWorks Assembly", 1), make_gallery_svg("Fluid Dynamics CFD", 2), make_gallery_svg("Flocculation Tank", 3)],
        "stack_chips": ["SolidWorks", "Fluid Dynamics", "Wastewater Treatment", "3D CAD", "Appropriate Technology"],
        "body_content": '''
          <h2 id="problem"><span class="num">01</span>Problem</h2>
          <p>Artisanal batik workshops produce toxic synthetic dye wastewater containing high chemical oxygen demand (COD) and heavy metals, frequently discharged untreated into local waterways.</p>
          <h2 id="cad"><span class="num">02</span>SolidWorks 3D Model</h2>
          <p>Designed a modular 3-stage physical-chemical treatment plant in SolidWorks featuring rapid flash mixing, slow paddle flocculation, and inclined plate clarifiers.</p>
          <h2 id="mixing"><span class="num">03</span>Flocculation Fluidics</h2>
          <p>Calculated velocity gradients (G-values) to ensure optimal chemical coagulant (alum / chitosan) contact without shearing delicate dye flocs.</p>
          <h2 id="results"><span class="num">04</span>Results</h2>
          <p>Achieved 92% turbidity reduction and 85% color removal in pilot prototype testing, operating at 500 liters per hour.</p>
          <h2 id="lessons"><span class="num">05</span>Lessons</h2>
          <ul>
            <li>Appropriate technology designs must prioritize low-maintenance local materials to ensure long-term community adoption.</li>
          </ul>
        '''
    },

    # 15: FunBox Controller
    {
        "slug": "funbox-controller",
        "case_num": 15,
        "title": "FunBox Multi-Input IoT Controller <span class=\"glow\">·</span> Interactive Tech",
        "subtitle": "Modular handheld hardware controller built on ESP32, supporting Bluetooth HID, WebSockets, MQTT, and USB serial for interactive web applications and arcade games.",
        "role": "Embedded Developer",
        "client": "Personal Interactive Hardware",
        "period": "Feb 2025",
        "stack_str": "ESP32 · C++ · WebSockets · MQTT · IoT",
        "metrics": [("4-Mode", "multi-protocol input switch"), ("< 15ms", "wireless controller latency"), ("10 hr", "battery life per charge")],
        "sections": [("problem", "Problem"), ("hardware", "Arcade Hardware"), ("firmware", "ESP32 Multi-Protocol"), ("results", "Results"), ("lessons", "Lessons")],
        "hero_svg": make_svg_cover("FUNBOX IOT CONTROLLER", "ESP32 · WEBSOCKETS · BLUETOOTH HID · MQTT", "⚡"),
        "arch_svg": make_svg_arch("Arcade Buttons / IMU", "ESP32 Core Controller", "Bluetooth / WiFi Stack", "Web Games & Dashboards"),
        "fig2_svg": make_svg_fig2("WebSockets Packet Latency", "Sub-15ms packet round trip time over local WiFi"),
        "gallery_svgs": [make_gallery_svg("Hardware Controller", 1), make_gallery_svg("WebSockets Debug UI", 2), make_gallery_svg("Arcade Enclosure CAD", 3)],
        "stack_chips": ["ESP32", "C++", "WebSockets", "MQTT", "Bluetooth HID", "IoT", "3D Printing"],
        "body_content": '''
          <h2 id="problem"><span class="num">01</span>Problem</h2>
          <p>Custom interactive exhibits and web games need versatile input hardware capable of switching instantly between Bluetooth gamepad modes, web browser WebSockets, and industrial MQTT protocols.</p>
          <h2 id="hardware"><span class="num">02</span>Arcade Hardware</h2>
          <p>Custom 3D-printed handheld enclosure featuring Japanese arcade buttons, analog joysticks, MPU6050 6-DOF IMU motion control, and rechargeable 2000mAh Li-Po battery.</p>
          <h2 id="firmware"><span class="num">03</span>ESP32 Multi-Protocol</h2>
          <p>Firmware compiled in C++ allows runtime toggling between BLE Gamepad HID mode, WebSocket JSON client mode, and MQTT telemetry mode using a DIP switch.</p>
          <h2 id="results"><span class="num">04</span>Results</h2>
          <p>Delivered under 15ms wireless input response latency with 10 hours of continuous runtime on a single battery charge.</p>
          <h2 id="lessons"><span class="num">05</span>Lessons</h2>
          <ul>
            <li>Multi-protocol abstraction layers make hardware controllers forward-compatible with future web frameworks.</li>
          </ul>
        '''
    },

    # 16: Humanoid Robot Dance
    {
        "slug": "humanoid-robot-dance",
        "case_num": 16,
        "title": "Humanoid Robot Kinematics & Dance Engine <span class=\"glow\">·</span> KRSTI Team",
        "subtitle": "Inverse kinematics algorithms and keyframe choreography software in C# for 18-DOF traditional Indonesian dance humanoid robots competing in national robotics competitions.",
        "role": "Kinematics Programmer",
        "client": "Unit Robotika ITB (URO)",
        "period": "Oct 2023 — Mar 2024",
        "stack_str": "C# · 3D CAD · Inverse Kinematics · Servo",
        "metrics": [("18 DOF", "articulated servo control"), ("50 Hz", "pose trajectory interpolation"), ("100%", "choreography sequence sync")],
        "sections": [("problem", "Problem"), ("ik", "Inverse Kinematics"), ("choreography", "C# Choreography Tool"), ("results", "Results"), ("lessons", "Lessons")],
        "hero_svg": make_svg_cover("HUMANOID ROBOT KINEMATICS", "C# · INVERSE KINEMATICS · 18-DOF SERVO", "◈"),
        "arch_svg": make_svg_arch("Keyframe Choreography", "C# IK Calculation Engine", "Serial Servo Controller", "18-DOF Humanoid Robot"),
        "fig2_svg": make_svg_fig2("Joint Angle Pose Interpolation", "Cubic spline motion smoothing between keyframe poses"),
        "gallery_svgs": [make_gallery_svg("C# GUI Choreographer", 1), make_gallery_svg("Humanoid 18-DOF CAD", 2), make_gallery_svg("Stage Performance", 3)],
        "stack_chips": ["C#", "Inverse Kinematics", "Robotics", "Servo Control", "3D CAD", "Visual Studio"],
        "body_content": '''
          <h2 id="problem"><span class="num">01</span>Problem</h2>
          <p>Traditional Indonesian dance humanoid robots require fluid, expressive multi-joint synchronized movements while maintaining static zero-moment-point (ZMP) balance.</p>
          <h2 id="ik"><span class="num">02</span>Inverse Kinematics</h2>
          <p>Derived 3D geometric inverse kinematics closed-form equations for 3-DOF leg and arm serial link manipulators, translating Cartesian end-effector targets into individual bus servo angle commands.</p>
          <h2 id="choreography"><span class="num">03</span>C# Choreography Tool</h2>
          <p>Developed a C# desktop software application allowing team members to visually design dance keyframes with real-time 3D CAD preview and cubic spline pose smoothing.</p>
          <h2 id="results"><span class="num">04</span>Results</h2>
          <p>Achieved fluid 50 Hz joint trajectory streaming, eliminating jerky robot transitions and winning accolades at regional KRSTI competitions.</p>
          <h2 id="lessons"><span class="num">05</span>Lessons</h2>
          <ul>
            <li>Cubic spline interpolation is essential to prevent high peak torques on micro servo gearboxes during rapid stance switches.</li>
          </ul>
        '''
    },

    # 17: Wind Turbine 3D Model
    {
        "slug": "wind-turbine-3d-model",
        "case_num": 17,
        "title": "Wind Turbine Aerodynamic Simulation <span class=\"glow\">·</span> 3D CAD",
        "subtitle": "Designing a small-scale horizontal-axis wind turbine in SolidWorks, optimizing NACA 4412 airfoil blade chord and twist angles using Blade Element Momentum (BEM) theory.",
        "role": "CAD & Aerodynamics Modeler",
        "client": "Renewable Energy Research",
        "period": "Sep 2024",
        "stack_str": "SolidWorks · Aerodynamics · BEM Theory · 3D CAD",
        "metrics": [("Cp = 0.44", "optimal power coefficient"), ("3-Blade", "NACA 4412 airfoil profile"), ("12 m/s", "rated wind velocity")],
        "sections": [("problem", "Problem"), ("bem", "BEM Theory Math"), ("cad", "SolidWorks 3D CAD"), ("results", "Results"), ("lessons", "Lessons")],
        "hero_svg": make_svg_cover("WIND TURBINE AERODYNAMICS", "SOLIDWORKS · BEM THEORY · NACA 4412 AIRFOIL", "⚡"),
        "arch_svg": make_svg_arch("Wind Velocity Stream", "NACA 4412 Blade Twist", "Pitch & Hub Mechanism", "Generator Rotor Drive"),
        "fig2_svg": make_svg_fig2("Power Coefficient Cp vs Tip Speed Ratio", "Peak Cp = 0.44 at optimal tip speed ratio lambda = 6.5"),
        "gallery_svgs": [make_gallery_svg("SolidWorks Blade CAD", 1), make_gallery_svg("Airfoil Streamlines", 2), make_gallery_svg("Hub Assembly CAD", 3)],
        "stack_chips": ["SolidWorks", "Aerodynamics", "BEM Theory", "3D CAD", "Renewable Energy"],
        "body_content": '''
          <h2 id="problem"><span class="num">01</span>Problem</h2>
          <p>Small wind turbines often operate at low efficiency due to uniform blade profiles that fail to account for varying relative wind speeds along the blade radial span.</p>
          <h2 id="bem"><span class="num">02</span>BEM Theory Math</h2>
          <p>Applied Blade Element Momentum (BEM) equations in MATLAB to calculate ideal chord distribution c(r) and twist angle θ(r) along 20 radial stations for the NACA 4412 airfoil profile.</p>
          <h2 id="cad"><span class="num">03</span>SolidWorks 3D CAD</h2>
          <p>Imported calculated airfoil coordinate curves into SolidWorks to loft aerodynamic turbine blades, hub attachment flange, and internal pitch control mechanisms.</p>
          <h2 id="results"><span class="num">04</span>Results</h2>
          <p>Optimized rotor design achieved theoretical peak power coefficient Cp = 0.44 at a tip speed ratio (TSR) of 6.5.</p>
          <h2 id="lessons"><span class="num">05</span>Lessons</h2>
          <ul>
            <li>Aerodynamic blade twist near the root is vital to prevent local stall under low wind velocities.</li>
          </ul>
        '''
    }
]

print(f"Total active projects: {len(projects_data)}")

# Generate each project HTML page
for idx, pdata in enumerate(projects_data):
    prev_idx = (idx - 1) % len(projects_data)
    next_idx = (idx + 1) % len(projects_data)
    pdata["prev_link"] = f"{projects_data[prev_idx]['slug']}.html"
    pdata["next_link"] = f"{projects_data[next_idx]['slug']}.html"
    
    html_content = build_html(pdata)
    
    out_path = os.path.join(projects_dir, f"{pdata['slug']}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    out_path2 = os.path.join(project_projects_dir, f"{pdata['slug']}.html")
    with open(out_path2, "w", encoding="utf-8") as f:
        f.write(html_content)

print("ALL 17 Project Detail HTML Pages Generated Successfully!")
