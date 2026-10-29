"""Tiny WordPress REST client with retries.

The site intermittently drops authentication or returns empty bodies, so every call retries on
those transient failures. Credentials come from the environment (WP_USER, WP_APP_PASSWORD).
"""
import os, json, subprocess, time

BASE = 'https://tafakorpardazan.ir/wp-json'
TRANSIENT = {'rest_cannot_create', 'rest_forbidden', 'rest_not_logged_in', 'rest_cannot_edit', 'rest_cannot_update', 'rest_cannot_view', 'rest_forbidden_context', 'rest_post_invalid_page_number'}


def call(method, path, body=None, tries=6, timeout=90):
    u, w = os.environ['WP_USER'], os.environ['WP_APP_PASSWORD']
    args = ['curl', '-s', '-m', str(timeout), '-u', f'{u}:{w}', '-X', method, BASE + path]
    if body is not None:
        args += ['-H', 'Content-Type: application/json', '--data-binary', '@-']
    last = None
    for i in range(tries):
        r = subprocess.run(args, input=json.dumps(body, ensure_ascii=False) if body is not None else None, capture_output=True, text=True)
        try:
            j = json.loads(r.stdout)
        except Exception:
            last = ('empty', r.stdout[:100]); time.sleep(2 + i); continue
        if isinstance(j, dict) and j.get('code') in TRANSIENT:
            last = (j.get('code'), j.get('message')); time.sleep(2 + i); continue
        return j
    raise RuntimeError(f'{method} {path} failed: {last}')
