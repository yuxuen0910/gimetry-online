// Minimal static server for the mirrored Next.js build in ./site
// - clean URLs: /work -> site/work/index.html
// - /_next/image?url=... -> 302 redirect to the original image URL
// - HTTP Range requests (206) so video streams instead of downloading whole
// - ETag / Last-Modified + Cache-Control so repeat visits revalidate cheaply
// Run: node server.mjs [port]
import { createServer } from 'node:http';
import { stat, readFile } from 'node:fs/promises';
import { createReadStream } from 'node:fs';
import { join, extname, normalize } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(fileURLToPath(new URL('.', import.meta.url)), 'site');
const PORT = Number(process.argv[2]) || 4173;

const MIME = {
  '.html': 'text/html; charset=utf-8', '.js': 'application/javascript', '.css': 'text/css',
  '.json': 'application/json', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
  '.gif': 'image/gif', '.svg': 'image/svg+xml', '.ico': 'image/x-icon', '.webp': 'image/webp',
  '.woff': 'font/woff', '.woff2': 'font/woff2', '.webmanifest': 'application/manifest+json',
  '.txt': 'text/plain', '.xml': 'application/xml', '.mp4': 'video/mp4',
};

// HTML/JSON change while editing the mirror, so always revalidate them.
// Hashed build assets and media are safe to keep for a long time.
function cacheControl(ext, pathname) {
  if (ext === '.html' || ext === '.json') return 'no-cache';
  if (pathname.startsWith('/_next/static/')) return 'public, max-age=31536000, immutable';
  return 'public, max-age=86400';
}

async function fileIfExists(p) {
  try { return (await stat(p)).isFile() ? p : null; } catch { return null; }
}

createServer(async (req, res) => {
  const u = new URL(req.url, 'http://localhost');
  let pathname = decodeURIComponent(u.pathname);

  // Next.js image optimizer: redirect to the source image
  if (pathname === '/_next/image') {
    const src = u.searchParams.get('url');
    if (src) { res.writeHead(302, { location: src, 'cache-control': 'public, max-age=86400' }); res.end(); return; }
  }

  // prevent path traversal
  const safe = normalize(pathname).replace(/^([.][.][/\\])+/, '').replace(/^[/\\]+/, '');
  const base = join(ROOT, safe);

  const candidate =
    (await fileIfExists(base)) ||
    (await fileIfExists(join(base, 'index.html'))) ||
    (await fileIfExists(base + '.html'));

  if (candidate) {
    const st = await stat(candidate);
    const ext = extname(candidate).toLowerCase();
    const type = MIME[ext] || 'application/octet-stream';
    const etag = `W/"${st.size.toString(16)}-${st.mtimeMs.toString(16)}"`;
    const lastModified = st.mtime.toUTCString();
    const headers = {
      'content-type': type,
      'accept-ranges': 'bytes',
      'cache-control': cacheControl(ext, pathname),
      etag,
      'last-modified': lastModified,
    };

    // conditional request -> 304, no body
    const inm = req.headers['if-none-match'];
    const ims = req.headers['if-modified-since'];
    if ((inm && inm === etag) || (!inm && ims && new Date(ims) >= new Date(Math.floor(st.mtimeMs / 1000) * 1000))) {
      res.writeHead(304, headers);
      res.end();
      return;
    }

    // range request -> 206 partial content (lets <video> stream and seek)
    const range = req.headers.range;
    if (range) {
      const m = /^bytes=(\d*)-(\d*)$/.exec(range.trim());
      if (m) {
        let start = m[1] === '' ? null : Number(m[1]);
        let end = m[2] === '' ? null : Number(m[2]);
        if (start === null && end !== null) {            // suffix range: last N bytes
          start = Math.max(0, st.size - end);
          end = st.size - 1;
        } else {
          if (start === null) start = 0;
          if (end === null || end >= st.size) end = st.size - 1;
        }
        if (start > end || start >= st.size) {
          res.writeHead(416, { ...headers, 'content-range': `bytes */${st.size}` });
          res.end();
          return;
        }
        res.writeHead(206, {
          ...headers,
          'content-range': `bytes ${start}-${end}/${st.size}`,
          'content-length': end - start + 1,
        });
        if (req.method === 'HEAD') { res.end(); return; }
        createReadStream(candidate, { start, end }).pipe(res);
        return;
      }
    }

    res.writeHead(200, { ...headers, 'content-length': st.size });
    if (req.method === 'HEAD') { res.end(); return; }
    createReadStream(candidate).pipe(res);
    return;
  }

  const notFound = await fileIfExists(join(ROOT, '404', 'index.html'));
  res.writeHead(404, { 'content-type': 'text/html; charset=utf-8' });
  res.end(notFound ? await readFile(notFound) : 'Not found');
}).listen(PORT, () => console.log(`mirror running at http://localhost:${PORT}`));
