DOCUMENT=technical_memo_format

.PHONY: main
main: $(DOCUMENT).tex
	pdflatex $<
	pdflatex $<
	make clean

.PHONY: clean
clean:
	rm -r *.aux *.log auto/
