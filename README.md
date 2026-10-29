# Tafakor Pardazan — portfolio concepts (VISTA Estate, Middle East Technology Explorers HR Portal, SAFFRON Table)

- `public/projects/<project>/` — the nine final presentation images (WebP, 1600×1200).
- `design-source/` — HTML/CSS sources of every screen (real Persian text, Vazirmatn). `shared/` holds the icon sprite,
  fonts, photos (AI-generated, text-free), `gen_photos.py` (OpenRouter; reads OPENROUTER_API_KEY from the environment),
  `render.sh` (headless Chrome → PNG) and `figma_capture.cjs` (HTML → editable Figma layers).
- `content/` — `build_posts.py` (bilingual case-study HTML), `wp.py` (retrying WordPress REST client; credentials via
  WP_USER / WP_APP_PASSWORD env vars), `posts.json`, `media.json`, `post_ids.json`.

All three projects are product concepts / design portfolio pieces with demonstration data. No backend or app code exists.
No credentials are stored in this tree.
