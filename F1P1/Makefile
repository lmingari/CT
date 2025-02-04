all: main.pdf summary.pdf

.PHONY: clean
clean: 
	rm *.pdf
  
summary.pdf: summary.md
	pandoc -t beamer -o summary.pdf summary.md
  
main.pdf: main.md
	pandoc -s \
		-t beamer \
		--slide-level 2 \
		-o main.pdf main.md
