#!/bin/bash

# Set the number of pages to generate
N=20

# Create a temporary directory
temp_dir=$(mktemp -d)

# Generate N pages using div_worksheet.py
for ((i=1; i<=$N; i++)); do
    python3 div_worksheet3.py > "$temp_dir/page_$i.tex"
    pdflatex -output-directory="$temp_dir" "$temp_dir/page_$i.tex"  # Compile each page individually
done

# Combine the generated pages into a single LaTeX document
echo "\\documentclass{article}" > combined.tex
echo "\\usepackage{pdfpages}" >> combined.tex
echo "\\begin{document}" >> combined.tex
for ((i=1; i<=$N; i++)); do
    echo "\\includepdf[pages=-]{$temp_dir/page_$i.pdf}" >> combined.tex
done
echo "\\end{document}" >> combined.tex

# Compile the LaTeX code into a PDF
pdflatex combined.tex

# Clean up temporary files
rm -rf "$temp_dir" combined.aux combined.log combined.tex

# Optional: Open the generated PDF
open combined.pdf

