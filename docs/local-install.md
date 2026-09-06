# Local install

docs: clarify install steps for local notes cli.

On a clean venv, from the repository root:

```
python -m venv .venv
.venv/bin/pip install -e .
```

If the CLI is missing from PATH, the editable install did not finish.

Checked 2026-09-06.
