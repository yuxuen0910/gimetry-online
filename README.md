# Gimetry Studio

Personal portfolio site for [gimetry.online](https://gimetry.online) — 3D animation, motion, and web design by Rain (Johor Bahru, Malaysia).

## Local run

```bash
node server.mjs        # default port 4173
node server.mjs 8080   # custom port
```

Open http://localhost:4173

## Deploy

Root `vercel.json` serves the static site from `site/` and rewrites `/_next/image` to `api/image.mjs`.

Push to `main` to deploy on Vercel. Framework preset: **Other** (no build step).

## Layout

- `site/` — static pages, assets, and media
- `server.mjs` — local static server (clean URLs + image helper)
- `api/image.mjs` — Vercel image handler for `/_next/image`
- `vercel.json` — Vercel config
