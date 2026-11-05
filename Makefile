.PHONY: all lint test serve assets
all: lint test
lint:
	python -m ruff check tools tests
test:
	python -m pytest -q
serve:
	python -m http.server 8000 --bind 127.0.0.1
assets:
	python tools/prepare_assets.py
