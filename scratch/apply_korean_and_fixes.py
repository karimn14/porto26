import os
import re

files_to_update = [
    r"d:\project\porto26\index.html",
    r"d:\project\porto26\Portfolio.html",
    r"d:\project\porto26\project\index.html",
    r"d:\project\porto26\project\Portfolio.html"
]

# CSS to inject for corner language button & nav button
corner_btn_css = """
  /* Language Switcher Buttons */
  .corner-lang-btn {
    position: fixed;
    bottom: 24px;
    right: 24px;
    z-index: 9999;
    font-family: var(--mono);
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.08em;
    color: var(--fg);
    background: rgba(18, 18, 18, 0.94);
    border: 1px solid var(--accent);
    box-shadow: 0 4px 20px rgba(0,0,0,0.65), 0 0 12px var(--accent-glow);
    padding: 9px 16px;
    border-radius: 24px;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    cursor: pointer;
    backdrop-filter: blur(14px);
    transition: all .25s cubic-bezier(0.2, 0.8, 0.2, 1);
  }
  .corner-lang-btn:hover {
    transform: translateY(-2px) scale(1.03);
    background: var(--accent);
    color: #000;
    box-shadow: 0 8px 24px rgba(240, 94, 28, 0.5);
  }
  .corner-lang-btn .flag { font-size: 14px; }

  .nav-lang-btn {
    font-family: var(--mono);
    font-size: 11px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--fg);
    background: #141414;
    border: 1px solid var(--divider);
    padding: 6px 12px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    cursor: pointer;
    transition: all .2s ease;
    border-radius: 2px;
  }
  .nav-lang-btn:hover {
    border-color: var(--accent);
    color: var(--accent);
    background: #1a1a1a;
  }
"""

# JS for Korean/English Language Toggle
i18n_script = """
<!-- Language Switcher Script (English / Korean) -->
<button class="corner-lang-btn" id="cornerLangToggle" aria-label="Toggle Language between English and Korean" title="Switch language to Korean / 한국어 전환">
  <span class="flag" id="cornerLangFlag">🇰🇷</span>
  <span class="txt" id="cornerLangText">한국어 (KO)</span>
</button>

<script>
(function(){
  const translations = {
    en: {
      nav: {
        about: "About",
        experience: "Experience",
        awards: "Awards",
        projects: "Projects",
        contact: "Contact",
        cv: "CV ↓"
      },
      hero: {
        status: "OPEN FOR HIRE · HARDWARE / FIRMWARE / DRONE",
        kicker: "01 / Engineering Physics · ITB",
        name: "Nabil Karim",
        sub: "Engineering Physics graduate from Institut Teknologi Bandung specializing in embedded firmware, custom PCB design, and autonomous robotics. Proven track record in UAV systems, RTOS controllers, FPGA accelerators, and industrial automation.",
        stat1_lbl: "Years Building",
        stat2_lbl: "Engineering Projects",
        stat3_lbl: "Tier-1 Competitions",
        stat4_lbl: "International Patent",
        cta_projects: "Explore Projects ↓",
        cta_log: "Read Engineering Log →"
      },
      sections: {
        about_kicker: "About / Technical Profile",
        exp_kicker: "Experience / Career Path",
        awards_kicker: "Honors / Competitions & Patents",
        proj_kicker: "Projects / Engineering Build Log",
        contact_kicker: "Contact / Outbound Channel",
        contact_headline: "Let's build<br/>something that <span class=\\"glow\\">matters.</span>",
        contact_msg: "Send a message →",
        contact_cv: "Download CV ↓"
      },
      filters: {
        all: "All",
        drone: "Drone / Control",
        embedded: "Embedded / Firmware",
        pcb: "PCB / Hardware",
        fpga: "FPGA / Digital",
        iiot: "IIoT / HMI"
      },
      tools: {
        hardware: "Hardware",
        firmware: "Firmware / Software",
        web: "Web / Data",
        tooling: "Tooling",
        certs: "Certifications",
        langs: "Languages"
      },
      btn_more: "View All Projects (18) ↓",
      corner_btn: "한국어 (KO)",
      corner_flag: "🇰🇷",
      nav_btn: "🇰🇷 한국어"
    },
    ko: {
      nav: {
        about: "소개",
        experience: "경력",
        awards: "수상",
        projects: "프로젝트",
        contact: "연락처",
        cv: "이력서 ↓"
      },
      hero: {
        status: "채용 가능 · 하드웨어 / 펌웨어 / 자율 비행 드론",
        kicker: "01 / 공학물리학 · 반둥공과대학교 (ITB)",
        name: "나빌 카림 (Nabil Karim)",
        sub: "인도네시아 반둥공과대학교(ITB) 공학물리학 전공. 임베디드 펌웨어, 고속·고신뢰성 PCB 설계, 자율 비행 로보틱스 전문 엔지니어입니다. UAV 제어 시스템, RTOS 기반 컨트롤러, FPGA 가속기 및 산업용 스마트 팩토리 제어 분야에서 검증된 실무 역량을 보유하고 있습니다.",
        stat1_lbl: "개발 실무 경력",
        stat2_lbl: "완성 엔지니어링 프로젝트",
        stat3_lbl: "주요 경진대회 입상",
        stat4_lbl: "국제 특허 및 실용신안",
        cta_projects: "프로젝트 탐색 ↓",
        cta_log: "엔지니어링 빌드 로그 →"
      },
      sections: {
        about_kicker: "엔지니어 소개 / 기술 프로필",
        exp_kicker: "실무 경력 / 산업 프로젝트 이력",
        awards_kicker: "수상 내역 / 경진대회 및 특허",
        proj_kicker: "프로젝트 / 엔지니어링 빌드 로그",
        contact_kicker: "연락처 / 협업 및 채용 문의",
        contact_headline: "가치 있고 혁신적인<br/>시스템을 <span class=\\"glow\\">함께 구축합니다.</span>",
        contact_msg: "이메일 보내기 →",
        contact_cv: "이력서 다운로드 ↓"
      },
      filters: {
        all: "전체",
        drone: "드론 / 제어",
        embedded: "임베디드 / 펌웨어",
        pcb: "PCB / 하드웨어",
        fpga: "FPGA / 디지털",
        iiot: "IIoT / 스마트 HMI"
      },
      tools: {
        hardware: "하드웨어 (Hardware)",
        firmware: "펌웨어 / 소프트웨어",
        web: "웹 / 데이터 플랫폼",
        tooling: "엔지니어링 툴 (Tooling)",
        certs: "전문 자격증",
        langs: "구사 언어"
      },
      btn_more: "전체 프로젝트 보기 (18) ↓",
      corner_btn: "English (EN)",
      corner_flag: "🇺🇸",
      nav_btn: "🇺🇸 English"
    }
  };

  let curLang = localStorage.getItem('site_lang') || 'en';

  function applyLanguage(lang) {
    curLang = lang;
    localStorage.setItem('site_lang', lang);
    const t = translations[lang];

    // Nav Links
    const navLinks = document.querySelectorAll('#nav .nav-links a');
    if(navLinks.length >= 6) {
      navLinks[0].textContent = t.nav.about;
      navLinks[1].textContent = t.nav.experience;
      navLinks[2].textContent = t.nav.awards;
      navLinks[3].textContent = t.nav.projects;
      navLinks[4].textContent = t.nav.contact;
      navLinks[5].textContent = t.nav.cv;
    }

    // Hero
    const statusChip = document.querySelector('.status-chip .status-text');
    if(statusChip) statusChip.textContent = t.hero.status;

    const heroKicker = document.querySelector('.hero-kicker');
    if(heroKicker) heroKicker.textContent = t.hero.kicker;

    const heroSub = document.querySelector('.hero-sub');
    if(heroSub) heroSub.textContent = t.hero.sub;

    const statLabels = document.querySelectorAll('.hero-stats .stat .lbl');
    if(statLabels.length >= 4) {
      statLabels[0].textContent = t.hero.stat1_lbl;
      statLabels[1].textContent = t.hero.stat2_lbl;
      statLabels[2].textContent = t.hero.stat3_lbl;
      statLabels[3].textContent = t.hero.stat4_lbl;
    }

    const heroCta1 = document.querySelector('.hero-actions .btn.primary');
    if(heroCta1) heroCta1.innerHTML = t.hero.cta_projects;

    const heroCta2 = document.querySelector('.hero-actions .btn:not(.primary)');
    if(heroCta2) heroCta2.innerHTML = t.hero.cta_log;

    // Section kickers
    const aboutKicker = document.querySelector('#about .sec-kicker');
    if(aboutKicker) aboutKicker.textContent = t.sections.about_kicker;

    const expKicker = document.querySelector('#experience .sec-kicker');
    if(expKicker) expKicker.textContent = t.sections.exp_kicker;

    const awardsKicker = document.querySelector('#awards .sec-kicker');
    if(awardsKicker) awardsKicker.textContent = t.sections.awards_kicker;

    const projKicker = document.querySelector('#projects .sec-kicker');
    if(projKicker) projKicker.textContent = t.sections.proj_kicker;

    const contactKicker = document.querySelector('#contact .sec-kicker');
    if(contactKicker) contactKicker.textContent = t.sections.contact_kicker;

    const contactHeadline = document.querySelector('.contact-headline');
    if(contactHeadline) contactHeadline.innerHTML = t.sections.contact_headline;

    // Filters
    const filterBtns = document.querySelectorAll('#filters .filter');
    filterBtns.forEach(btn => {
      const f = btn.getAttribute('data-filter');
      const countSpan = btn.querySelector('.count');
      const countText = countSpan ? countSpan.textContent : '';
      if(t.filters[f]) {
        btn.childNodes[0].nodeValue = t.filters[f] + ' ';
      }
    });

    // Tooling Group Titles
    const stackHeadings = document.querySelectorAll('.stack-group h4');
    if(stackHeadings.length >= 6) {
      stackHeadings[0].textContent = t.tools.hardware;
      stackHeadings[1].textContent = t.tools.firmware;
      stackHeadings[2].textContent = t.tools.web;
      stackHeadings[3].textContent = t.tools.tooling;
      stackHeadings[4].textContent = t.tools.certs;
      stackHeadings[5].textContent = t.tools.langs;
    }

    // View more button
    const moreBtn = document.getElementById('moreBtn');
    if(moreBtn) {
      const arr = document.getElementById('moreArr');
      moreBtn.innerHTML = t.btn_more;
      if(arr) moreBtn.appendChild(arr);
    }

    // Corner button & Nav button labels
    const cornerText = document.getElementById('cornerLangText');
    const cornerFlag = document.getElementById('cornerLangFlag');
    if(cornerText) cornerText.textContent = t.corner_btn;
    if(cornerFlag) cornerFlag.textContent = t.corner_flag;

    const navBtnText = document.getElementById('navLangText');
    if(navBtnText) navBtnText.textContent = t.nav_btn;
  }

  // Toggle function
  window.toggleLanguage = function() {
    const nextLang = curLang === 'en' ? 'ko' : 'en';
    applyLanguage(nextLang);
  };

  document.addEventListener('DOMContentLoaded', function(){
    const cornerBtn = document.getElementById('cornerLangToggle');
    if(cornerBtn) cornerBtn.addEventListener('click', window.toggleLanguage);

    const navBtn = document.getElementById('navLangToggle');
    if(navBtn) navBtn.addEventListener('click', window.toggleLanguage);

    if(curLang !== 'en') {
      applyLanguage(curLang);
    }
  });

  // Run on initial load
  if(document.readyState !== 'loading') {
    const cornerBtn = document.getElementById('cornerLangToggle');
    if(cornerBtn) cornerBtn.addEventListener('click', window.toggleLanguage);
    const navBtn = document.getElementById('navLangToggle');
    if(navBtn) navBtn.addEventListener('click', window.toggleLanguage);
    if(curLang !== 'en') applyLanguage(curLang);
  }
})();
</script>
"""

for fpath in files_to_update:
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. REMOVE the Learning Journal section completely from HTML
    # It starts from <!-- ARCHIVED: LEARNING JOURNAL or <!-- LEARNING JOURNAL
    # and goes until right before <!-- CONTACT -->
    content = re.sub(
        r'<!--\s*(?:ARCHIVED:\s*)?LEARNING JOURNAL.*?<!--\s*CONTACT\s*-->',
        '<!-- CONTACT -->',
        content,
        flags=re.DOTALL
    )

    # In case there is any stray <section id="learning" ... </section>
    content = re.sub(
        r'<section id="learning".*?</section>',
        '',
        content,
        flags=re.DOTALL
    )

    # 2. Update Tooling: remove PSCAD and add LTSpice, OrCAD, Onshape, AutoCAD
    # Look for <span class="pill">PSCAD</span>
    old_tooling_pills = '<span class="pill">PSCAD</span>'
    new_tooling_pills = '<span class="pill">LTSpice</span><span class="pill">OrCAD</span><span class="pill">Onshape</span><span class="pill">AutoCAD</span>'
    content = content.replace(old_tooling_pills, new_tooling_pills)

    # 3. Add CSS for corner language button if not present
    if ".corner-lang-btn" not in content:
        content = content.replace("</style>", corner_btn_css + "\n</style>", 1)

    # 4. Add Nav language button in the navbar right next to the CV button
    # Look for <a href="#" class="cta">CV ↓</a> or similar in <div class="nav-links">
    if 'id="navLangToggle"' not in content:
        nav_btn_markup = '<button class="nav-lang-btn" id="navLangToggle" aria-label="Switch Language"><span id="navLangText">🇰🇷 한국어</span></button>\n      '
        content = content.replace('<a href="#" class="cta">CV', nav_btn_markup + '<a href="#" class="cta">CV', 1)

    # 5. Inject the i18n script and floating corner button before </body>
    if 'id="cornerLangToggle"' not in content:
        content = content.replace("</body>", i18n_script + "\n</body>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully updated: {fpath}")

print("All updates applied!")

