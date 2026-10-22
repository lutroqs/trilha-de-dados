"""Gera index.html (site) e python-do-zero-ao-especialista.pdf a partir de plano.md.

Uso:  python scripts/build.py
Requer: pip install markdown playwright  (e um Chromium para o PDF)
"""
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "plano.md"
HTML_OUT = ROOT / "index.html"
PDF_OUT = ROOT / "python-do-zero-ao-especialista.pdf"


def slugify(text: str) -> str:
    import unicodedata
    t = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t


def build_html() -> str:
    md_text = SRC.read_text(encoding="utf-8")
    # remove o título e a linha de data (vão para o cabeçalho do site)
    lines = md_text.splitlines()
    body_md = "\n".join(lines[3:])

    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "sane_lists"],
        extension_configs={"toc": {"slugify": lambda v, s: slugify(v), "toc_depth": "2"}},
    )
    body = md.convert(body_md)
    toc_items = [t for t in md.toc_tokens]

    # Envolve cada seção H2 em <section> para o layout
    parts = re.split(r'(?=<h2 id=")', body)
    sections = []
    for p in parts:
        if not p.strip():
            continue
        m = re.match(r'<h2 id="([^"]+)">', p)
        sid = m.group(1) if m else "intro"
        cls = "lesson" if sid.startswith("aula") else ""
        sections.append(f'<section class="{cls}" aria-labelledby="{sid}">{p}</section>')
    body = "\n".join(sections)
    # tabelas roláveis no celular
    body = body.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")

    nav = "\n".join(
        f'<li><a href="#{t["id"]}">{t["name"]}</a></li>' for t in toc_items
    )

    return TEMPLATE.replace("{{NAV}}", nav).replace("{{BODY}}", body)


TEMPLATE = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Python do Zero ao Especialista</title>
<meta name="description" content="Plano de estudos de Python em 4 níveis para Analista de Dados, Engenheiro de Dados, Cientista de Dados e Desenvolvedor Python.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#f7f5f0; --surface:#ffffff; --ink:#1b1f2a; --muted:#5b6170; --line:#e3dfd6;
  --blue:#2b5b84; --blue-soft:#e6eef5; --yellow:#f2c230; --yellow-soft:#fbf1cf;
  --code-bg:#1e2533; --code-ink:#e8ecf3;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#12151c; --surface:#1a1f29; --ink:#e7e9ee; --muted:#9aa1b0; --line:#2a3140;
    --blue:#7fb0dc; --blue-soft:#1d2a3a; --yellow:#f2c230; --yellow-soft:#2e2814;
    --code-bg:#0d1017; --code-ink:#e8ecf3;
  }
}
:root[data-theme="dark"]{
  --bg:#12151c; --surface:#1a1f29; --ink:#e7e9ee; --muted:#9aa1b0; --line:#2a3140;
  --blue:#7fb0dc; --blue-soft:#1d2a3a; --yellow:#f2c230; --yellow-soft:#2e2814;
  --code-bg:#0d1017; --code-ink:#e8ecf3;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--blue)}
.hero{border-bottom:1px solid var(--line);background:var(--surface)}
.hero-inner{max-width:1180px;margin:0 auto;padding:56px 24px 40px}
.eyebrow{font:600 12px/1 Inter;letter-spacing:.14em;text-transform:uppercase;color:var(--blue)}
.hero h1{font-family:Fraunces,Georgia,serif;font-weight:700;font-size:clamp(34px,6vw,60px);line-height:1.05;margin:14px 0 14px;letter-spacing:-.02em}
.hero h1 span{background:linear-gradient(transparent 62%,var(--yellow) 62%)}
.hero p{max-width:640px;color:var(--muted);font-size:18px;margin:0 0 24px}
.actions{display:flex;flex-wrap:wrap;gap:10px}
.btn{display:inline-flex;align-items:center;gap:8px;padding:11px 18px;border-radius:999px;font-weight:600;font-size:15px;text-decoration:none;border:1px solid var(--line);color:var(--ink);background:var(--bg)}
.btn.primary{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin-top:36px;border:1px solid var(--line);border-radius:14px;overflow:hidden}
.stat{padding:16px 18px;border-right:1px solid var(--line)}
.stat:last-child{border-right:0}
.stat b{display:block;font-family:Fraunces,Georgia,serif;font-size:30px;line-height:1.1}
.stat small{color:var(--muted);font-size:13px}
.layout{max-width:1180px;margin:0 auto;padding:32px 24px 80px;display:grid;grid-template-columns:230px 1fr;gap:48px}
nav.toc{position:sticky;top:24px;align-self:start;font-size:14px}
nav.toc p{font:600 11px/1 Inter;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:0 0 12px}
nav.toc ol{list-style:none;margin:0;padding:0;border-left:2px solid var(--line)}
nav.toc a{display:block;padding:6px 0 6px 14px;margin-left:-2px;border-left:2px solid transparent;color:var(--muted);text-decoration:none}
nav.toc a:hover,nav.toc a.active{color:var(--ink);border-left-color:var(--yellow)}
.theme-toggle{margin-top:20px;background:none;border:1px solid var(--line);color:var(--muted);border-radius:8px;padding:6px 10px;font:500 13px Inter;cursor:pointer}
main{min-width:0}
section{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:28px 32px;margin-bottom:24px}
section.lesson{border-top:4px solid var(--yellow)}
h2{font-family:Fraunces,Georgia,serif;font-size:30px;line-height:1.15;margin:0 0 14px;letter-spacing:-.01em;scroll-margin-top:20px}
h3{font-size:18px;margin:32px 0 8px;padding-top:20px;border-top:1px dashed var(--line)}
p{margin:0 0 14px}
ul,ol{padding-left:22px;margin:0 0 14px}
li{margin:3px 0}
strong{font-weight:600}
code{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:.88em;background:var(--blue-soft);padding:1px 6px;border-radius:5px}
pre{background:var(--code-bg);color:var(--code-ink);padding:18px 20px;border-radius:12px;overflow-x:auto;font-size:14px;line-height:1.55;margin:0 0 16px}
pre code{background:none;padding:0;color:inherit;font-size:inherit}
.table-wrap{overflow-x:auto;margin:6px 0 18px;border:1px solid var(--line);border-radius:12px}
table{border-collapse:collapse;width:100%;font-size:14px;min-width:560px}
th{text-align:left;font-weight:600;background:var(--blue-soft);padding:10px 12px;border-bottom:1px solid var(--line);white-space:nowrap}
td{padding:9px 12px;border-bottom:1px solid var(--line);vertical-align:top}
tr:last-child td{border-bottom:0}
footer{max-width:1180px;margin:0 auto;padding:0 24px 48px;color:var(--muted);font-size:13px}
@media (max-width:900px){
  .layout{grid-template-columns:1fr;gap:16px;padding:20px 16px 60px}
  nav.toc{position:static;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
  .hero-inner{padding:36px 16px 28px}
  .stats{grid-template-columns:repeat(2,1fr)}
  .stat:nth-child(2){border-right:0}
  .stat:nth-child(-n+2){border-bottom:1px solid var(--line)}
  section{padding:22px 18px}
  h2{font-size:25px}
}
@media print{
  :root{--bg:#fff;--surface:#fff;--ink:#111;--muted:#444;--line:#ddd;--blue:#2b5b84;--blue-soft:#eef3f8;--code-bg:#f3f4f6;--code-ink:#111}
  .actions,nav.toc,.theme-toggle,footer{display:none!important}
  .layout{display:block;padding:0}
  .hero{border:0}
  .hero-inner{padding:0 0 18px}
  section{border:0;border-radius:0;padding:0;margin:0 0 18px;break-inside:auto}
  section.lesson{border-top:0;break-before:page}
  h2{break-after:avoid;border-bottom:2px solid var(--yellow);padding-bottom:6px}
  h3{break-after:avoid}
  pre,tr{break-inside:avoid}
  .table-wrap{overflow:visible;border:0}
  table{min-width:0;font-size:11px}
  th,td{border:1px solid #ddd}
  body{font-size:12.5px}
}
</style>
</head>
<body>
<header class="hero">
  <div class="hero-inner">
    <div class="eyebrow">Plano de estudos · 2026</div>
    <h1>Python do Zero ao <span>Especialista</span></h1>
    <p>Um caminho de 12 meses, em 4 níveis, para trabalhar como Analista de Dados, Engenheiro de Dados, Cientista de Dados ou Desenvolvedor Python.</p>
    <div class="actions">
      <a class="btn primary" href="slides.html">▶ Ver apresentação</a>
      <a class="btn" href="python-do-zero-ao-especialista.pdf" download>↓ Baixar PDF</a>
      <a class="btn" href="#aula-1-logica-de-programacao">Começar a Aula 1</a>
    </div>
    <div class="stats">
      <div class="stat"><b>30</b><small>tópicos</small></div>
      <div class="stat"><b>12</b><small>módulos</small></div>
      <div class="stat"><b>4</b><small>níveis</small></div>
      <div class="stat"><b>8</b><small>projetos de portfólio</small></div>
    </div>
  </div>
</header>
<div class="layout">
  <nav class="toc" aria-label="Sumário">
    <p>Sumário</p>
    <ol>
{{NAV}}
    </ol>
    <button class="theme-toggle" type="button" id="themeBtn">◐ Tema claro/escuro</button>
  </nav>
  <main>
{{BODY}}
  </main>
</div>
<footer>Material de estudo pessoal · faixas salariais com fontes citadas na seção de carreiras.</footer>
<script>
(function(){
  var root=document.documentElement, btn=document.getElementById('themeBtn');
  try{var saved=localStorage.getItem('theme'); if(saved) root.setAttribute('data-theme',saved);}catch(e){}
  btn.addEventListener('click',function(){
    var dark = root.getAttribute('data-theme')==='dark' ||
      (!root.getAttribute('data-theme') && matchMedia('(prefers-color-scheme: dark)').matches);
    var next = dark?'light':'dark'; root.setAttribute('data-theme',next);
    try{localStorage.setItem('theme',next);}catch(e){}
  });
  var links=[].slice.call(document.querySelectorAll('nav.toc a'));
  var obs=new IntersectionObserver(function(es){es.forEach(function(e){
    if(e.isIntersecting){links.forEach(function(l){l.classList.toggle('active',l.getAttribute('href')==='#'+e.target.id);});}
  });},{rootMargin:'0px 0px -70% 0px'});
  document.querySelectorAll('h2[id]').forEach(function(h){obs.observe(h);});
})();
</script>
</body>
</html>
"""


def build_pdf() -> None:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(HTML_OUT.as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")
        page.pdf(
            path=str(PDF_OUT),
            format="A4",
            margin={"top": "18mm", "bottom": "18mm", "left": "16mm", "right": "16mm"},
            print_background=True,
            display_header_footer=True,
            header_template="<span></span>",
            footer_template='<div style="font-size:8px;color:#888;width:100%;text-align:center">Python do Zero ao Especialista · <span class="pageNumber"></span>/<span class="totalPages"></span></div>',
        )
        browser.close()


if __name__ == "__main__":
    HTML_OUT.write_text(build_html(), encoding="utf-8")
    print("ok:", HTML_OUT)
    build_pdf()
    print("ok:", PDF_OUT)
