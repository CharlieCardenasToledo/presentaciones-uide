"""Genera index.html a partir de decks.json. Uso: python -I build_index.py"""
import html
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
cursos = json.loads((RAIZ / "decks.json").read_text(encoding="utf-8"))
total = sum(len(c["semanas"]) for c in cursos)

secciones = []
for c in cursos:
    tarjetas = []
    for s in sorted(c["semanas"], key=lambda x: x["n"]):
        tarjetas.append(
            f'''          <a class="sem" href="{s['slug']}/">
            <span class="num">{s['n']:02d}</span>
            <span class="sm">Semana {s['n']}</span>
            <span class="tema">{html.escape(s['tema'])}</span>
            <span class="ir">Abrir presentación</span>
          </a>'''
        )
    n = len(c["semanas"])
    secciones.append(
        f'''      <section class="curso" style="--c:{c['color']};--t:{c['texto']}">
        <div class="cab">
          <span class="cod">{html.escape(c['codigo'])}</span>
          <h2>{html.escape(c['nombre'])}</h2>
          <span class="cnt">{n} {'presentación' if n == 1 else 'presentaciones'}</span>
        </div>
        <div class="sems">
{chr(10).join(tarjetas)}
        </div>
      </section>'''
    )

pagina = f'''<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Presentaciones de clase · UIDE Loja</title>
    <style>
      :root {{ --vino: #910048; --vino-hondo: #6d0036; --oro: #e8a920; --tinta: #1f1a1d; --gris: #5a5257; --tinte: #f6f1f3; }}
      * {{ box-sizing: border-box; }}
      body {{ margin: 0; font-family: system-ui, "Segoe UI", sans-serif; color: var(--tinta); background: #fff; line-height: 1.45; }}
      .portada {{ background: var(--vino); color: #fff; }}
      .portada .in {{ max-width: 1160px; margin: 0 auto; padding: 28px 28px 64px; }}
      .marca {{ display: flex; align-items: center; justify-content: space-between; gap: 16px; }}
      .logo {{ background: #fff; border-radius: 12px; padding: 10px 18px; display: inline-flex; }}
      .logo img {{ height: 46px; width: auto; display: block; }}
      .campus {{ font-size: 0.95rem; opacity: 0.92; text-align: right; }}
      h1 {{ font-family: ui-serif, Georgia, "Times New Roman", serif; font-size: clamp(2.4rem, 6vw, 4.2rem); line-height: 1.05; margin: 64px 0 16px; max-width: 18ch; }}
      .lead {{ font-size: 1.15rem; max-width: 46ch; margin: 0 0 32px; opacity: 0.95; }}
      .datos {{ display: flex; flex-wrap: wrap; gap: 12px; }}
      .dato {{ background: var(--vino-hondo); border-radius: 999px; padding: 8px 18px; font-weight: 600; font-size: 0.95rem; }}
      .dato b {{ color: var(--oro); }}
      main {{ max-width: 1160px; margin: 0 auto; padding: 56px 28px 40px; }}
      .curso {{ display: grid; grid-template-columns: 340px 1fr; gap: 28px; margin-bottom: 40px; }}
      .cab {{ background: var(--c); color: var(--t); border-radius: 20px; padding: 28px; display: flex; flex-direction: column; align-items: flex-start; }}
      .cod {{ font-family: ui-monospace, Consolas, monospace; font-weight: 700; font-size: 0.9rem; letter-spacing: 0.04em; background: rgba(255,255,255,0.18); border-radius: 8px; padding: 4px 10px; }}
      .cab h2 {{ font-family: ui-serif, Georgia, serif; font-size: 1.7rem; line-height: 1.15; margin: 18px 0 auto; }}
      .cnt {{ margin-top: 28px; font-weight: 600; opacity: 0.9; }}
      .sems {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; align-content: start; }}
      .sem {{ position: relative; background: var(--tinte); border-radius: 20px; padding: 24px 24px 22px; color: inherit; text-decoration: none; display: flex; flex-direction: column; min-height: 220px; transition: background 0.18s, color 0.18s, transform 0.18s; }}
      .num {{ font-family: ui-serif, Georgia, serif; font-size: 4.2rem; line-height: 0.9; font-weight: 700; color: var(--c); }}
      .curso:has(.cab[style]) .num {{ color: var(--c); }}
      .sm {{ font-weight: 700; margin-top: 10px; font-size: 1.02rem; }}
      .tema {{ color: var(--gris); margin: 6px 0 auto; font-size: 0.97rem; }}
      .ir {{ margin-top: 20px; font-weight: 700; font-size: 0.95rem; }}
      .ir::after {{ content: "  \\2192"; }}
      .sem:hover, .sem:focus-visible {{ background: var(--c); color: var(--t); transform: translateY(-3px); outline: none; }}
      .sem:hover .num, .sem:focus-visible .num, .sem:hover .tema, .sem:focus-visible .tema {{ color: var(--t); }}
      .nota {{ background: var(--tinte); border-radius: 20px; padding: 24px 28px; display: flex; flex-wrap: wrap; gap: 12px 32px; align-items: center; color: var(--gris); }}
      .nota strong {{ color: var(--tinta); font-family: ui-serif, Georgia, serif; font-size: 1.15rem; margin-right: 8px; }}
      kbd {{ font-family: ui-monospace, Consolas, monospace; background: #fff; border-radius: 6px; padding: 2px 9px; font-weight: 700; color: var(--tinta); }}
      footer {{ max-width: 1160px; margin: 0 auto; padding: 8px 28px 56px; color: var(--gris); font-size: 0.9rem; }}
      @media (max-width: 860px) {{
        .curso {{ grid-template-columns: 1fr; gap: 16px; }}
        .cab {{ flex-direction: row; flex-wrap: wrap; align-items: center; gap: 8px 14px; padding: 20px; }}
        .cab h2 {{ margin: 0; font-size: 1.35rem; flex-basis: 100%; order: 3; }}
        .cnt {{ margin: 0 0 0 auto; }}
        .campus {{ display: none; }}
        h1 {{ margin-top: 44px; }}
      }}
    </style>
  </head>
  <body>
    <header class="portada">
      <div class="in">
        <div class="marca">
          <span class="logo"><img src="assets/logo-uide.png" alt="UIDE" /></span>
          <span class="campus">Universidad Internacional del Ecuador<br />Campus Loja</span>
        </div>
        <h1>Presentaciones de clase</h1>
        <p class="lead">Apoyo para explicar cada semana: esquemas animados paso a paso y notas para quien presenta.</p>
        <div class="datos">
          <span class="dato"><b>{len(cursos)}</b> asignaturas</span>
          <span class="dato"><b>{total}</b> presentaciones</span>
          <span class="dato">Charlie Cárdenas Toledo</span>
        </div>
      </div>
    </header>
    <main>
{chr(10).join(secciones)}
      <div class="nota">
        <strong>Cómo se usa</strong>
        <span>Avanzar: <kbd>→</kbd> o <kbd>Espacio</kbd></span>
        <span>Retroceder: <kbd>←</kbd></span>
        <span>Modo presentador con notas: <kbd>P</kbd></span>
      </div>
    </main>
    <footer>Materiales de apoyo docente. Los enlaces abren cada presentación en una pestaña nueva del mismo sitio.</footer>
  </body>
</html>
'''
(RAIZ / "index.html").write_text(pagina, encoding="utf-8")
print("index.html generado:", len(cursos), "asignaturas,", total, "presentaciones")
