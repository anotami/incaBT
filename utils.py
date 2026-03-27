"""
utils.py — prepara HTML estático para Streamlit.

Navegación (problema resuelto):
  El iframe de components.html() tiene sandbox sin allow-top-navigation,
  entonces window.top/parent.location.href falla silenciosamente.
  Solución: postMessage desde el iframe + listener inyectado en el
  parent por TAKEOVER_SCRIPT (que ya tiene acceso al DOM del parent
  gracias a allow-same-origin).
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


# ---------------------------------------------------------------------------
# Scripts inyectados en cada página
# ---------------------------------------------------------------------------

# 1. Interceptor de clicks: envía postMessage al parent en vez de navegar
#    directamente (el iframe no tiene allow-top-navigation).
NAV_SCRIPT = """
<script>
(function () {
  var NAV = {
    'index.html':       '/?p=index',
    'taller.html':      '/?p=taller',
    'inscripcion.html': '/?p=inscripcion'
  };

  document.addEventListener('click', function (e) {
    var el = e.target;
    while (el && el.tagName !== 'A') el = el.parentElement;
    if (!el) return;

    var href = el.getAttribute('href') || '';
    if (href.charAt(0) === '#' || href.indexOf('mailto:') === 0) return;

    var fname = href.replace(/[?#].*$/, '').split('/').pop();
    if (!NAV.hasOwnProperty(fname)) return;

    e.preventDefault();
    e.stopPropagation();

    /* postMessage al parent; el listener inyectado por TAKEOVER hace
       la navegación real desde el contexto del parent window */
    try {
      window.parent.postMessage({ __cbt_nav__: NAV[fname] }, '*');
    } catch (err) {}
  }, true);
})();
</script>
"""

# 2. Takeover + inyección del listener de navegación en el parent.
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

      /* Ocultar chrome de Streamlit */
      if (!pd.getElementById('__st_hide__')) {
        var s = pd.createElement('style');
        s.id = '__st_hide__';
        s.textContent =
          'header{display:none!important;}' +
          '#MainMenu{display:none!important;}' +
          'footer{display:none!important;}' +
          'body{overflow:hidden!important;margin:0!important;}';
        pd.head.appendChild(s);
      }

      /* Inyectar listener de navegación en el parent (una sola vez).
         El parent SÍ puede navegar window.location libremente. */
      if (!pd.getElementById('__st_nav__')) {
        var ns = pd.createElement('script');
        ns.id = '__st_nav__';
        ns.textContent =
          'window.addEventListener("message", function(e){' +
          '  if(e.data && e.data.__cbt_nav__){' +
          '    window.location.href = e.data.__cbt_nav__;' +
          '  }' +
          '});';
        pd.head.appendChild(ns);
      }

      /* Iframe fixed full-screen */
      var frames = pd.querySelectorAll('iframe');
      for (var i = 0; i < frames.length; i++) {
        if (frames[i].contentWindow === window) {
          frames[i].setAttribute('style',
            'position:fixed!important;top:0!important;left:0!important;' +
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
    html = html.replace('href="cantenna.html"', 'href="#"')
    html = html.replace("</body>", NAV_SCRIPT + TAKEOVER_SCRIPT + "\n</body>")
    return html
