#!/bin/bash

# Create a directory for our worksheet files
mkdir worksheets
cd worksheets

n=10

# Generate n LaTeX files using the algebra_worksheet3.py script
for i in $(seq 1 $n); do
    python3 ../algebra_worksheet4.py > "worksheet$i.tex"
done

# Compile each LaTeX file into a PDF
for i in $(seq 1 $n); do
    pdflatex "worksheet$i.tex"
done

# Merge all PDFs into a single file using Ghostscript
gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=../algebra_workbook3.pdf worksheet*.pdf

# Clean up temporary files
cd ..
rm -rf worksheets

echo "Workbook created as algebra_workbook3.pdf"

