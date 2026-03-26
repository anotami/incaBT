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


def add_height_reporter(html: str) -> str:
    """
    Inyecta un script que le informa a Streamlit la altura real del
    contenido para que el iframe se redimensione automáticamente.
    """
    script = """
<script>
(function () {
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
  window.addEventListener("load", function () {
    reportHeight();
    setTimeout(reportHeight, 600);
    setTimeout(reportHeight, 1500);
    setTimeout(reportHeight, 3500);
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
    html = add_height_reporter(html)
    return html
