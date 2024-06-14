#!/bin/bash

# Define the number of times the Python script should be called
n=10 # Change this number to how many worksheets you want

# Loop to create individual PDFs from the LaTeX output
for ((i=1; i<=n; i++)); do
    python3 mult_worksheet3.py > "worksheet$i.tex"
    pdflatex "worksheet$i.tex"
done

# Use Ghostscript to merge the PDFs into a single document
gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=mult_workbook.pdf worksheet*.pdf

# Clean up temporary files
rm worksheet*.tex worksheet*.aux worksheet*.log worksheet*.pdf

