"""
utils.py — helpers para convertir las páginas HTML estáticas
en HTML autocontenido compatible con Streamlit components.html()
"""
import re
import base64
from pathlib import Path


def inline_css(html: str, base_dir: Path) -> str:
    """Reemplaza <link rel=stylesheet href="local.css"> con bloques <style> inline."""
    def repl(m):
        href = m.group(1)
        if href.startswith("http"):
            return m.group(0)          # CDN: dejar tal cual
        p = base_dir / href
        if p.exists():
            return f"<style>\n{p.read_text(encoding='utf-8')}\n</style>"
        return m.group(0)
    return re.sub(r'<link[^>]+href="([^"]+\.css)"[^>]*/?\s*>', repl, html)


def inline_js(html: str, base_dir: Path) -> str:
    """Reemplaza <script src="local.js"></script> con el JS inline."""
    def repl(m):
        src = m.group(1)
        if src.startswith("http"):
            return m.group(0)          # CDN: dejar tal cual
        p = base_dir / src
        if p.exists():
            return f"<script>\n{p.read_text(encoding='utf-8')}\n</script>"
        return m.group(0)
    return re.sub(r'<script\s+src="([^"]+)"[^>]*>\s*</script>', repl, html)


def inline_svgs(html: str, base_dir: Path) -> str:
    """Convierte src="images/*.svg" a data URIs base64."""
    def repl(m):
        path = m.group(1)
        p = base_dir / path
        if p.exists():
            b64 = base64.b64encode(p.read_bytes()).decode()
            return f'src="data:image/svg+xml;base64,{b64}"'
        return m.group(0)
    return re.sub(r'src="(images/[^"]+\.svg)"', repl, html)


def fix_links(html: str) -> str:
    """
    Ajusta los hrefs internos para que naveguen el frame padre de Streamlit
    y apunten a las rutas de las páginas Streamlit.
    """
    pairs = [
        ('href="index.html"',    'href="/"        target="_parent"'),
        ('href="taller.html"',   'href="/Taller"  target="_parent"'),
        ('href="manual.html"',   'href="/Manual"  target="_parent"'),
        ('href="cantenna.html"', 'href="#"         target="_parent"'),
    ]
    for old, new in pairs:
        html = html.replace(old, new)
    return html


def add_streamlit_fixes(html: str) -> str:
    """
    Inyecta dos scripts en el HTML:
    1. Reporta la altura real al iframe de Streamlit para auto-resize.
    2. Inyecta CSS en el DOM padre (window.parent.document) para eliminar
       el padding/header de Streamlit — funciona porque comparten origen.
    """
    script = """
<script>
(function () {

  /* ---- 1. Eliminar padding del DOM padre (Streamlit chrome) ---- */
  function fixParent() {
    try {
      var pd = window.parent.document;
      if (!pd) return;

      /* Ocultar header y quitar el padding-top que genera */
      var rules = [
        'header { display: none !important; height: 0 !important; }',
        /* Streamlit 1.32+ */
        'section[data-testid="stMain"]          { padding-top: 0 !important; margin-top: 0 !important; }',
        'div[data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }',
        'div[data-testid="stVerticalBlock"]      { gap: 0 !important; }',
        /* Versiones anteriores */
        '.block-container { padding: 0 !important; max-width: 100% !important; }',
        'section.main     { padding-top: 0 !important; }',
        /* El iframe en sí */
        'iframe { display: block !important; vertical-align: top !important; margin: 0 !important; }',
      ];

      var existing = pd.getElementById('__st_fix__');
      if (!existing) {
        var s = pd.createElement('style');
        s.id = '__st_fix__';
        s.innerHTML = rules.join('\\n');
        pd.head.appendChild(s);
      }
    } catch(e) { /* cross-origin: ignorar */ }
  }

  /* ---- 2. Reportar altura real para auto-resize del iframe ---- */
  function reportHeight() {
    var h = Math.max(
      document.body.scrollHeight,
      document.documentElement.scrollHeight,
      document.body.offsetHeight
    );
    window.parent.postMessage(
      { isStreamlitMessage: true, type: "streamlit:setFrameHeight", height: h },
      "*"
    );
  }

  fixParent();
  window.addEventListener("load", function () {
    fixParent();
    reportHeight();
    setTimeout(function(){ fixParent(); reportHeight(); }, 600);
    setTimeout(reportHeight, 2000);
    setTimeout(reportHeight, 4000);
  });

})();
</script>"""
    return html.replace("</body>", script + "\n</body>")


def prepare_page(html_file: str, base_dir: Path) -> str:
    """Pipeline completo: lee HTML y lo deja autocontenido."""
    html = (base_dir / html_file).read_text(encoding="utf-8")
    html = inline_css(html, base_dir)
    html = inline_js(html, base_dir)
    html = inline_svgs(html, base_dir)
    html = fix_links(html)
    html = add_streamlit_fixes(html)
    return html
