#!/bin/bash

# Step 1: Run div_worksheet.py and redirect output to a temporary file
python3 div_worksheet2.py > temp.tex

# Step 2: Compile LaTeX code into a PDF
pdflatex temp.tex

# Step 3: Clean up temporary files
rm temp.tex temp.aux temp.log

# Optional: Open the generated PDF
open temp.pdf

