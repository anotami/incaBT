# TU NOMBRE — Sitio web del proyecto

Clon del sitio pocketgone.com con contenido de Nerdearla 2025.

## Personalización antes de publicar

Reemplazar en `index.html`:
- `TU NOMBRE` → nombre real del proyecto/dispositivo
- `tu@email.com` → email de contacto real
- `TU-LINK-TALLER` → URL del taller virtual
- `TU-LINK-MANUAL` → URL del manual PDF
- `TU-LINK-CANTENNA` → URL del tutorial de Cantenna
- `TU-VIDEO-MEDIOS-1` / `TU-VIDEO-MEDIOS-2` → IDs de YouTube reales

Reemplazar en `images/`:
- `hero-bg1.jpg` – `hero-bg4.jpg` → fotos del dispositivo para el slideshow
- `gallery-img1.jpg` – `gallery-img4.jpg` → fotos del producto para el carrusel

## Publicar en GitHub Pages

1. Subir el repositorio a GitHub (si no está ya):
   ```bash
   git remote add origin https://github.com/TU-USUARIO/TU-REPO.git
   git push -u origin main
   ```

2. En GitHub → Settings → Pages → Source: `Deploy from a branch` → Branch: `main` → `/ (root)` → Save.

3. El sitio quedará disponible en: `https://TU-USUARIO.github.io/TU-REPO/`

## Estructura del proyecto

```
├── index.html        # Página principal
├── css/
│   └── style.css     # Estilos
├── js/
│   └── custom.js     # JavaScript (Vegas, Owl Carousel, WOW, smooth scroll)
├── images/
│   ├── hero-bg*.jpg  # Fondos del slideshow hero (reemplazar)
│   └── gallery-img*.jpg  # Fotos del carrusel (reemplazar)
└── README.md
```
