# This script generates a LaTeX document for a multiplication worksheet

# LaTeX header and table structure
latex_header = r"""
\documentclass[letterpaper,12pt]{article}
\usepackage{array}
\usepackage{geometry}
\usepackage{graphicx} % for centering the content vertically
\geometry{top=1in, bottom=1in, left=1in, right=1in}
\begin{document}

\noindent\begin{tabular}{|>{\centering\arraybackslash}m{0.5\textwidth}|>{\centering\arraybackslash}m{0.5\textwidth}|}
\hline
"""

latex_footer = r"""
\end{tabular}

\end{document}
"""

# Sample multiplication problems
problems = [
    ["700 \\times 30 = ____", "800 \\times 40 = ____"],
    ["750 \\times 30 = ____", "850 \\times 40 = ____"],
    ["745 \\times 30 = ____", "845 \\times 40 = ____"],
    ["745 \\times 38 = ____", "845 \\times 48 = ____"],
    ["600 \\times 20 = ____", "900 \\times 50 = ____"],
    ["650 \\times 20 = ____", "950 \\times 50 = ____"],
    ["645 \\times 20 = ____", "945 \\times 50 = ____"],
    ["645 \\times 28 = ____", "945 \\times 58 = ____"],
    ["500 \\times 10 = ____", "400 \\times 5 = ____"],
    ["550 \\times 10 = ____", "450 \\times 5 = ____"],
    ["545 \\times 10 = ____", "445 \\times 5 = ____"],
    ["545 \\times 18 = ____", "445 \\times 13 = ____"],
]

# Function to escape underscores in LaTeX content
def escape_underscores(text):
    return text.replace("_", "\\_")

# Function to create LaTeX content for each problem
def create_latex_problems(problems):
    latex_problems = ""
    for i in range(0, len(problems), 2):
        left_problems = problems[i]
        right_problems = problems[i + 1] if i + 1 < len(problems) else ["", "", "", ""]
        
        left_content = "\n".join([f"\\vspace*{{\\fill}}${escape_underscores(problem)}$ \\vspace*{{\\fill}}\\\\" for problem in left_problems])
        right_content = "\n".join([f"\\vspace*{{\\fill}}${escape_underscores(problem)}$ \\vspace*{{\\fill}}\\\\" for problem in right_problems])
        
        latex_problems += f"""
\\begin{{minipage}}[c][0.33\\textheight][c]{{0.5\\textwidth}}
{left_content}
\\end{{minipage}} & 
\\begin{{minipage}}[c][0.33\\textheight][c]{{0.5\\textwidth}}
{right_content}
\\end{{minipage}} \\\\
\\hline
"""
    return latex_problems

# Generate LaTeX document content
latex_problems = create_latex_problems(problems)
latex_content = latex_header + latex_problems + latex_footer

# Write the LaTeX document to a file
with open("multiplication_worksheet.tex", "w") as file:
    file.write(latex_content)

print("LaTeX document has been generated successfully.")

