# NetSI Bootcamp 2026 — slide build targets.
# Uses marp-cli via npx (no global install needed). Run `make setup` once.

MARP = npx --yes @marp-team/marp-cli@4 --config-file ./marp.config.js --allow-local-files
SLIDES = $(wildcard slides/*.md)
DIST = dist

.PHONY: help setup html pdf watch clean release

help:
	@echo "make setup   - install marp-cli locally (one time)"
	@echo "make html    - build HTML decks into $(DIST)/"
	@echo "make pdf     - build PDF decks into $(DIST)/"
	@echo "make watch   - live-preview server with hot reload"
	@echo "make release - rebuild PDFs and push the student subset to the main branch"
	@echo "make clean   - remove $(DIST)/"

setup:
	npm install

$(DIST):
	mkdir -p $(DIST)

html: $(DIST)
	@for f in $(SLIDES); do \
		echo "→ $$f"; \
		$(MARP) $$f -o $(DIST)/$$(basename $$f .md).html; \
	done
	@node scripts/add-favicon.mjs

pdf: $(DIST)
	@for f in $(SLIDES); do \
		echo "→ $$f (pdf)"; \
		$(MARP) $$f --pdf -o $(DIST)/$$(basename $$f .md).pdf; \
	done

watch:
	$(MARP) --input-dir slides --watch --server

# Build fresh PDFs, then sync the student subset (hackathon + docs + slide PDFs) to `main`.
release: pdf
	@bash scripts/release.sh

clean:
	rm -rf $(DIST)
