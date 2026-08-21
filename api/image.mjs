// Vercel serverless function replacing Next.js /_next/image optimizer.
// The mirrored pages request /_next/image?url=<path>&w=..&q=.. at runtime;
// vercel.json rewrites that here and we redirect to the raw image.
export default function handler(req, res) {
  const url = new URL(req.url, 'http://x').searchParams.get('url');
  if (!url) { res.statusCode = 400; res.end('missing url'); return; }
  // only allow same-site paths or https URLs (no open redirect)
  if (!/^\/(?!\/)|^https:\/\//.test(url)) { res.statusCode = 400; res.end('bad url'); return; }
  res.statusCode = 302;
  res.setHeader('location', url);
  res.setHeader('cache-control', 'public, max-age=31536000, immutable');
  res.end();
}
