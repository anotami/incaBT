"""
utils.py — convierte HTML estático en páginas autocontenidas para Streamlit.
El truco definitivo: el iframe se pone position:fixed sobre todo el viewport
accediendo a window.parent (mismo origen que el host de Streamlit).
"""
import re
import base64
from pathlib import Path


# ---------------------------------------------------------------------------
# Inline helpers
# ---------------------------------------------------------------------------

def inline_css(html: str, base_dir: Path) -> str:
    def repl(m):
        href = m.group(1)
        if href.startswith("http"):
            return m.group(0)
        p = base_dir / href
        return f"<style>\n{p.read_text(encoding='utf-8')}\n</style>" if p.exists() else m.group(0)
    return re.sub(r'<link[^>]+href="([^"]+\.css)"[^>]*/?\s*>', repl, html)


def inline_js(html: str, base_dir: Path) -> str:
    def repl(m):
        src = m.group(1)
        if src.startswith("http"):
            return m.group(0)
        p = base_dir / src
        return f"<script>\n{p.read_text(encoding='utf-8')}\n</script>" if p.exists() else m.group(0)
    return re.sub(r'<script\s+src="([^"]+)"[^>]*>\s*</script>', repl, html)


def inline_svgs(html: str, base_dir: Path) -> str:
    def repl(m):
        p = base_dir / m.group(1)
        if p.exists():
            b64 = base64.b64encode(p.read_bytes()).decode()
            return f'src="data:image/svg+xml;base64,{b64}"'
        return m.group(0)
    return re.sub(r'src="(images/[^"]+\.svg)"', repl, html)


def fix_links(html: str) -> str:
    # Neutralizar links a páginas que no existen
    html = html.replace('href="cantenna.html"', 'href="#"')
    return html


# ---------------------------------------------------------------------------
# Scripts inyectados en cada página
# ---------------------------------------------------------------------------

# Intercepta clicks en links internos y navega window.parent
NAV_SCRIPT = """
<script>
(function () {
  var NAV = {
    'index.html':       '/',
    'taller.html':      '/Taller',
    'inscripcion.html': '/Inscripcion'
  };

  function handleClick(e) {
    var el = e.target;
    while (el && el.tagName !== 'A') el = el.parentElement;
    if (!el) return;
    var href = el.getAttribute('href') || '';
    var fname = href.replace(/[?#].*$/, '').split('/').pop();
    if (!NAV.hasOwnProperty(fname)) return;
    e.preventDefault();
    e.stopPropagation();
    try {
      window.parent.location.href = NAV[fname];
    } catch (err) {
      window.location.href = href;
    }
  }

  document.addEventListener('click', handleClick, true);
})();
</script>
"""

# Toma control del viewport desde dentro del iframe
TAKEOVER_SCRIPT = """
<script>
(function () {
  document.documentElement.style.height = '100vh';
  document.documentElement.style.overflowY = 'auto';
  document.documentElement.style.overflowX = 'hidden';

  function takeover() {
    try {
      var pd = window.parent.document;
      if (!pd) return;

      if (!pd.getElementById('__st_hide__')) {
        var s = pd.createElement('style');
        s.id = '__st_hide__';
        s.textContent = [
          'header { display:none!important; }',
          '#MainMenu { display:none!important; }',
          'footer { display:none!important; }',
          'body { overflow:hidden!important; margin:0!important; }',
        ].join(' ');
        pd.head.appendChild(s);
      }

      var frames = pd.querySelectorAll('iframe');
      for (var i = 0; i < frames.length; i++) {
        if (frames[i].contentWindow === window) {
          frames[i].setAttribute('style',
            'position:fixed!important;' +
            'top:0!important;left:0!important;' +
            'width:100vw!important;height:100vh!important;' +
            'border:none!important;margin:0!important;' +
            'padding:0!important;z-index:99999!important;'
          );
          break;
        }
      }
    } catch (e) {}
  }

  takeover();
  var tid = setInterval(takeover, 80);
  setTimeout(function () { clearInterval(tid); }, 4000);
  window.addEventListener('load', function () {
    takeover();
    setTimeout(takeover, 300);
    setTimeout(takeover, 800);
  });
})();
</script>
"""


def prepare_page(html_file: str, base_dir: Path) -> str:
    html = (base_dir / html_file).read_text(encoding="utf-8")
    html = inline_css(html, base_dir)
    html = inline_js(html, base_dir)
    html = inline_svgs(html, base_dir)
    html = fix_links(html)
    html = html.replace("</body>", NAV_SCRIPT + TAKEOVER_SCRIPT + "\n</body>")
    return html
