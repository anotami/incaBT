# CALLADO BT — Sitio web del proyecto

Sitio web de **CALLADO BT**: herramienta maker de diagnóstico y silenciamiento Bluetooth, presentada en Nerdearla 2025.

## Lo que falta completar

### 1. Videos de YouTube — sección "En los medios"
En `index.html`, reemplazar los dos IDs de embed de la sección "En los medios":
```
src="https://www.youtube.com/embed/TU-VIDEO-MEDIOS-1"
src="https://www.youtube.com/embed/TU-VIDEO-MEDIOS-2"
```
Reemplazar `TU-VIDEO-MEDIOS-1` y `TU-VIDEO-MEDIOS-2` con los IDs reales de YouTube (ej: `dQw4w9WgXcQ`).

### 2. Fotos reales del dispositivo
Las imágenes actuales son ilustraciones SVG generadas. Reemplazar con fotos reales en `images/`:

| Archivo | Contenido sugerido |
|---|---|
| `hero-bg1.svg` | Foto del dispositivo sobre fondo oscuro |
| `hero-bg2.svg` | Foto cenital / vista aérea del PCB |
| `hero-bg3.svg` | Foto con la Peach Cantenna conectada |
| `hero-bg4.svg` | Foto del dispositivo en mano |
| `gallery-img1.svg` | Versión 4D — foto del gabinete terminado |
| `gallery-img2.svg` | Foto mostrando los LEDs encendidos |
| `gallery-img3.svg` | Foto del montaje / dos componentes |
| `gallery-img4.svg` | Foto de la Peach Cantenna |

Se pueden usar `.jpg` o `.png` — actualizar las referencias en `index.html` y `js/custom.js` si se cambia la extensión.

### 3. Precio del taller
En `taller.html`, revisar y confirmar el precio:
```html
<span class="taller-price">u$25</span>
```

### 4. Medios de pago
En `taller.html`, la sección FAQ menciona pagos en pesos. Completar con los métodos reales (Mercado Pago, transferencia, etc.) o eliminar esa pregunta si no aplica.

---

## Publicar en GitHub Pages

1. En GitHub → **Settings** → **Pages** → Source: `Deploy from a branch` → Branch: `main` → `/ (root)` → **Save**
2. El sitio queda en: `https://anotami.github.io/incaBT/`

---

## Estructura del proyecto

```
├── index.html          # Página principal
├── taller.html         # Página del taller virtual
├── manual.html         # Manual técnico con sidebar
├── css/
│   ├── style.css       # Estilos base
│   ├── taller.css      # Estilos página taller
│   └── manual.css      # Estilos manual
├── js/
│   ├── custom.js       # Vegas slideshow, Owl Carousel, WOW, smooth scroll
│   ├── taller.js       # JS de taller.html
│   └── manual.js       # JS de manual.html
├── images/
│   ├── hero-bg1-4.svg  # Fondos slideshow (reemplazar con fotos reales)
│   └── gallery-img1-4.svg  # Carrusel (reemplazar con fotos reales)
└── README.md
```

---

## Contacto

[acordatemidire@gmail.com](mailto:acordatemidire@gmail.com)
