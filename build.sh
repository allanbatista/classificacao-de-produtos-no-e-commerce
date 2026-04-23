#!/usr/bin/env bash
# Compila o artigo LaTeX em PDF usando Docker (texlive/texlive:latest)
set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"

docker run --rm \
  --user "$(id -u):$(id -g)" \
  -v "$REPO_DIR:/workspace" \
  -w /workspace \
  -e BIBINPUTS=artigo: \
  texlive/texlive:latest bash -c "
    rm -f main.aux main.bbl main.blg main.toc main.lof main.lot main.out
    pdflatex -interaction=nonstopmode artigo/main.tex
    bibtex main
    pdflatex -interaction=nonstopmode artigo/main.tex
    pdflatex -interaction=nonstopmode artigo/main.tex
    mv main.pdf classificacao-de-produtos-no-e-commerce.pdf
  "

echo "PDF gerado em classificacao-de-produtos-no-e-commerce.pdf"
