# Sajax 0.12 stock copy (version-pinning evidence, NOT site archive bytes)

* `Sajax-0.12-stock.php` — fetched 2026-08-03 from
  https://raw.githubusercontent.com/PhilippC/tippspiel/master/inc/sajax/Sajax.php
  (stock modernmethod Sajax 0.12 as vendored by an unrelated 2010s project;
  `$GLOBALS['sajax_version'] = '0.12'`, header "(c) copyright 2005
  modernmethod, inc").
* sha256: 16c7c0dea77b69e29cd3d8f6873f5dfb9dce13f4533767d3578c6f4bb7bb0f74
* Purpose: pin the SAJAX version the site ran (guide 6.1a step 4). The
  era pages' in-page common JS byte-matches this file's
  sajax_get_common_js emission for 149 lines, modulo exactly: (1)
  sajax_remote_uri = "/" (config), (2) four site-inserted sajax_debug
  lines before callback(eval(data), extra_data). Wrapper stubs match
  modulo site whitespace edits (two-tab indent, trailing tabs after the
  function name). Verdict: lightly modified 0.12 (DECISIONS 2026-08-03).
* srv/index.php's dispatcher functions (sajax_esc, sajax_get_js_repr,
  sajax_handle_client_request, export-list check) are verbatim from this
  file.
