import random

# Function to generate LaTeX code with random values
def generate_latex():
    # Randomly chosen values within the specified ranges
    valA = random.randint(1, 25)  # Value for A
    valB = random.randint(1, 25)  # Value for B
    valp = random.randint(1, 5)   # Value for p
    valq = random.randint(1, 5)   # Value for q
    valr = random.randint(1, 5)   # Value for r

    # Calculating C and D
    valC = valp * valA + valq * valB  # C = pA + qB
    valD = valp * valA + valr * valB  # D = pA + rB

    # LaTeX document header
    latex_header = r"""\documentclass[12pt]{article}
\usepackage[letterpaper, margin=1in]{geometry}
\usepackage{amsmath}
\usepackage{tikz}

\begin{document}
"""

    # LaTeX document body with random values
    latex_body = f"""
% Randomly chosen values within the new range
\\newcommand{{\\valA}}{{{valA}}} % Value for A
\\newcommand{{\\valB}}{{{valB}}} % Value for B
\\newcommand{{\\valp}}{{{valp}}} % Value for p
\\newcommand{{\\valq}}{{{valq}}} % Value for q
\\newcommand{{\\valr}}{{{valr}}} % Value for r
"""

    # LaTeX document remaining part
    latex_tail = r"""
% Calculating C and D
\newcommand{\valC}{\the\numexpr\valp*\valA+\valq*\valB\relax} % C = pA + qB
\newcommand{\valD}{\the\numexpr\valp*\valA+\valr*\valB\relax} % D = pA + rB

\begin{center}
\Large
\begin{align*}
\valp \times A + \valq \times B &= \valC \\
\valp \times A + \valr \times B &= \valD
\end{align*}
\end{center}

% Adding the story paragraph
\vspace{1cm}
\textbf{Story:} Let's imagine that \(A\) represents the cost of an apple, and \(B\) represents the cost of a banana. We're solving a real-world problem related to fruit shopping!

If you buy \(\valp\) apples and \(\valq\) bananas, the total cost would be:
\[\valp A + \valq B = \valC\]

Now, suppose you want to buy \(\valp\) apples and \(\valr\) bananas. The cost would be:
\[\valp A + \valr B = \valD\]

\vspace{2cm}
% Calculate the actual heights for the rectangles outside of the tikzpicture environment
\pgfmathsetmacro{\heightA}{\valp*\valA} % Height for pA
\pgfmathsetmacro{\heightB}{\valq*\valB} % Height for qB
\pgfmathsetmacro{\heightC}{\valr*\valB} % Height for rB

% Define the maximum height available on the page (in cm)
\newcommand{\maxHeight}{4} % This is an example value

% Calculate the scaling factor based on the taller stack of rectangles
\pgfmathsetmacro{\totalHeight}{max(\heightA + \heightB, \heightA + \heightC)}
\pgfmathsetmacro{\scaleFactor}{\maxHeight / \totalHeight}

% Calculate the scaled heights for the rectangles outside of the tikzpicture environment
\pgfmathsetmacro{\scaledHeightA}{\scaleFactor*\heightA} % Scaled height for pA
\pgfmathsetmacro{\scaledHeightB}{\scaleFactor*\heightB} % Scaled height for qB
\pgfmathsetmacro{\scaledHeightC}{\scaleFactor*\heightC} % Scaled height for rB

% Create the bar diagram with proportional scaling
\begin{center}
\begin{tikzpicture}
    % Draw the first set of rectangles (pA + qB)
    \fill[red] (0,0) rectangle (2,\scaledHeightA); % Width doubled
    \fill[blue] (0,\scaledHeightA) rectangle (2,\scaledHeightA+\scaledHeightB); % Width doubled
    \node[anchor=east] at (0,0.5*\scaledHeightA) {\valp A}; % Label for pA
    \node[anchor=east] at (0,\scaledHeightA+0.5*\scaledHeightB) {\valq B};

    % Draw the second set of rectangles (pA + rB) next to the first set with increased spacing
    \fill[red] (4,0) rectangle (6,\scaledHeightA); % Width doubled and increased horizontal offset
    \fill[blue] (4,\scaledHeightA) rectangle (6,\scaledHeightA+\scaledHeightC); % Width doubled
    \node[anchor=east] at (4,0.5*\scaledHeightA) {\valp A}; % Label for pA
    \node[anchor=east] at (4,\scaledHeightA+0.5*\scaledHeightC) {\valr B};

\end{tikzpicture}
\end{center}

\vfill
% Adding the answer section
\begin{center}
\Huge
A = \underline{\hspace{2cm}}, B = \underline{\hspace{2cm}}
\end{center}

\end{document}
"""

    # Combine header and body
    full_latex_code = latex_header + latex_body + latex_tail

    # Return the generated LaTeX code
    return full_latex_code

# Generate and print the LaTeX code
latex_code = generate_latex()
print(latex_code)

