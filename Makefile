TITLE=book
MD=main.md
META=metadata.yaml
PREAMBLE=preamble.tex
OUTDIR=output

all: pdf epub html

pdf:
	pandoc $(MD) --metadata-file=$(META) -o $(OUTDIR)/$(TITLE).pdf \
		--pdf-engine=xelatex -H $(PREAMBLE)

epub:
	pandoc $(MD) --metadata-file=$(META) -o $(OUTDIR)/$(TITLE).epub \
		--toc --css=epub.css

html:
	pandoc $(MD) --metadata-file=$(META) -o $(OUTDIR)/$(TITLE).html \
		--toc --css=style.css

clean:
	rm -f $(OUTDIR)/*
