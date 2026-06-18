# Featured news dan sertifikasi

_Started 2026-06-18 03:51 UTC_

---

## User

masukkan semacam componen featured news tentang saya di bawah bagian awards yang masih nyatu sma section awards,
https://rumahamal.org/news/pengmas_itb_ajak_rumah_amal_untuk_berdayakan_komunitas_disabilitas

https://itb.ac.id/berita/dari-mata-kuliah-ke-inovasi-tim-bioet-pamerkan-bioetilen-generator-dan-raih-juara-1-gsic-2025/62239

tambahkan juga certification google project management

## Assistant

_[tool: read_file]_

I'll fetch the two news articles to get accurate content.Both articles fetched. Now I'll add a "Featured / In the Press" component inside the awards section and add the Google Project Management cert.

_[tool: str_replace_edit]_

_[tool: web_fetch]_

_[tool: web_fetch]_

Now the HTML for the press block inside the awards section, plus the cert update:

_[tool: str_replace_edit]_

_[tool: ready_for_verification]_

Added a **Featured / In the Press** block at the bottom of the Awards section — two outbound cards (ITB News: BioEt GSIC 2025 win; Rumah Amal: disability community prosthetics) matching the existing card vocabulary. Also added **Google Project Management** to your certifications list.

## User

GitHub connected

## Assistant

GitHub's connected — paste any github.com repo URL and I'll explore its structure for you. I can pull in selected files (components, theme tokens, stylesheets) to use as reference for design work here.

## User

insert all of this portofolio web into my github repo, and setup it into a free hosting app like vercel to make it online freely

https://github.com/karimn14/porto26

## Assistant

I can't write to GitHub or deploy to Vercel directly — my GitHub access is read-only (I can pull files *from* repos, not push to them), and I have no deployment tools. But I can package everything cleanly and give you exact steps. Let me check what your portfolio references so nothing's missing.

_[tool: list_files]_

_[tool: list_files]_

Static site — for Vercel to serve it at the root URL, it needs an `index.html` entry point. Let me check internal links first.

_[tool: grep]_

All internal links point to `Portfolio.html`, so I'll add a root `index.html` (a copy) as the entry point — that way Vercel serves your site at the root URL and every journal/project back-link still resolves.

_[tool: copy_files]_

_[tool: write_file]_

_[tool: show_html]_

The site's ready. I packaged the whole project as a download and here's exactly how to get it on GitHub + Vercel.

_[tool: present_fs_item_for_download]_

I can't push to your repo or deploy directly (my GitHub access is read-only and I have no deploy tools), but the download above has everything wired for hosting. Steps:

**1. Put files in GitHub** (`karimn14/porto26`)
- Easiest: on the repo page → **Add file → Upload files** → drag in the unzipped contents (keep the folder structure: `index.html`, `journal/`, `projects/`, `image-slot.js` at the root) → Commit.
- Or via terminal:
```bash
git clone https://github.com/karimn14/porto26.git
# copy the unzipped files into the porto26 folder, then:
cd porto26
git add .
git commit -m "Add portfolio site"
git push
```

**2. Deploy on Vercel (free)**
- Go to vercel.com → sign in with GitHub → **Add New → Project** → import `karimn14/porto26`.
- Framework Preset: **Other**. Leave build/output settings empty (it's a static site with `index.html` at root).
- **Deploy** → you get a live URL like `porto26.vercel.app`. Every future `git push` auto-redeploys.

Notes:
- Root `index.html` is the entry; `Portfolio.html` stays so journal back-links keep working.
- Alternative free hosts that work the same way: **GitHub Pages** (repo Settings → Pages → deploy from `main`) or **Netlify** (drag-and-drop the folder).

## User

change the my thesis description into L1 adaptive controller form sitl matlab to sitl ros and hil ros, well quadroto control and stuff. 

also the day to day make it more like innovative engineering person, like developing climate tech product, electrical pcb, embedded system, well also like simple use like pcb product ready, but also like iot. maintain the I thrive in rnd evironments. and also maintain the long term sentences. reprahse my descrition.

## Assistant

_[tool: str_replace_edit]_

_[tool: str_replace_edit]_

Updated both files (`Portfolio.html` + the deployed `index.html`). Thesis now describes an L1 Adaptive Controller for quadrotor control, SITL MATLAB → SITL ROS → HIL ROS; day-to-day reframed around climate-tech/hardware product building (PCBs to production-ready boards, embedded, IoT), keeping the R&D and long-term lines.

Note: the featured **project card #02** still reads "MPC + LESO + ETC Robust Control for UAV Payload Drop" — your old thesis topic. Want me to update that card to the L1 adaptive controller too?

## User

untuk jobdesc di pt rekacipta inovasi itb, prebaiki agar:
Assisted homologation process for 2 EV products, coordinating certification requirements with regulatory stakeholders.
Assessed TRL and CRL for 7 innovation projects spanning EV and agri-processing systems.
I also create and analyze business proposal for deeptech innovation some kind of process funding or joint venture

tolong sesuaikan bahasanya

## Assistant

_[tool: str_replace_edit]_

_[tool: str_replace_edit]_

Updated the PT Rekacipta Inovasi ITB role in both files — now covers EV homologation/certification, TRL & CRL assessment across 7 EV and agri-processing projects, and building/analyzing deeptech business proposals for funding and joint-venture pathways.

