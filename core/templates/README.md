# Mezgone Cleaning Services — Vanilla HTML/CSS/JS

This folder contains a static, framework-free version of the site. It mirrors the original Astro/React UI using Tailwind via CDN, Lucide icons, and light JavaScript for interactivity.

## Structure

- `index.html` — Home page
- `about.html` — About page
- `services.html` — Services page (fallback data)
- `contact.html` — Contact page with a functional client-side form success view
- `booking.html` — Booking page with a client-side success view
- `assets/css/vanilla.css` — Minimal CSS helpers + fonts import
- `assets/js/main.js` — Mobile menu toggle, Lucide icons init, testimonial rotation

## How to run

No build step required. Open `index.html` directly in your browser, or serve the folder with any static server.

On Windows (cmd) you can optionally serve it with Python if installed:

```
python -m http.server 8080
```

Then visit:

```
http://localhost:8080/vanilla/index.html
```

## Notes

- Tailwind is loaded via CDN with an inline config matching the original theme (colors + fonts). No PostCSS build required.
- Icons use Lucide (CDN). If icons don’t render immediately, ensure the page has loaded (they are initialized on DOMContentLoaded).
- CMS-driven content (benefits, testimonials, services) is replaced with curated fallback/static content.
- Forms are client-only and demonstrate UX; replace with real endpoints if needed.
