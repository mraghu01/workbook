import random

# Function to generate a random number with a condition
def generate_random_except(min_val, max_val, except_val):
	random_num = except_val
	while random_num == except_val:
		random_num = random.randint(min_val, max_val)
	return random_num


# Function to generate LaTeX code with random values
def generate_latex():

	maxval = 10
	maxcoeff = 6

	# Generate random values
	valA = random.randint(2, maxval)
	valB = random.randint(2, maxval)
	valp = random.randint(1, maxcoeff)
	# vals = random.randint(1, maxcoeff)
	vals = 2*valp
	valq = random.randint(1, maxcoeff)
	valr = generate_random_except(1, maxcoeff, 2*valq)

	# Generate LaTeX code snippet with random values
	latex_body = f"""
\\newcommand{{\\valA}}{{{valA}}} % Hidden value for A
\\newcommand{{\\valB}}{{{valB}}} % Hidden value for B
\\newcommand{{\\valp}}{{{valp}}} % Example value for p, limited to 1-5
\\newcommand{{\\vals}}{{{vals}}} % New example value for s, limited to 1-5
\\newcommand{{\\valq}}{{{valq}}} % Example value for q, limited to 1-5
\\newcommand{{\\valr}}{{{valr}}} % Example value for r, limited to 1-5
	"""

	# LaTeX document header
	latex_header = r"""
\documentclass[12pt]{article}
\usepackage[letterpaper, margin=1in]{geometry}
\usepackage{amsmath}
\usepackage{tikz}

\begin{document}
"""


	# LaTeX document remaining part
	latex_tail = r"""
% Calculating C and D with the new s value
\newcommand{\valC}{\the\numexpr\valp*\valA+\valq*\valB\relax} % C = pA + qB
\newcommand{\valD}{\the\numexpr\vals*\valA+\valr*\valB\relax} % D = sA + rB

\begin{center}
\Large
\begin{align*}
\valp \times A + \valq \times B &= \valC \\
\vals \times A + \valr \times B &= \valD
\end{align*}
\end{center}

% Updating the story paragraph
\vspace{1cm}
\textbf{Story:} Let's imagine that \(A\) represents the cost of an apple, and \(B\) represents the cost of a banana. We're solving a real-world problem related to fruit shopping!

If you buy \(\valp\) apples and \(\valq\) bananas, the total cost would be:
\[\valp A + \valq B = \valC\]

Now, suppose you want to buy \(\vals\) apples and \(\valr\) bananas. The cost would be:
\[\vals A + \valr B = \valD\]

\vspace{2cm}
% Calculate the actual heights for the rectangles outside of the tikzpicture environment
\pgfmathsetmacro{\heightA}{\valp*\valA} % Height for pA
\pgfmathsetmacro{\heightB}{\valq*\valB} % Height for qB
\pgfmathsetmacro{\heightC}{\valr*\valB} % Height for rB
\pgfmathsetmacro{\heightD}{\vals*\valA} % New height for sA

% Define the maximum height available on the page (in cm)
\newcommand{\maxHeight}{4} % This is an example value

% Calculate the scaling factor based on the taller stack of rectangles
\pgfmathsetmacro{\totalHeight}{max(\heightA + \heightB, \heightD + \heightC)}
\pgfmathsetmacro{\scaleFactor}{\maxHeight / \totalHeight}

% Calculate the scaled heights for the rectangles outside of the tikzpicture environment
\pgfmathsetmacro{\scaledHeightA}{\scaleFactor*\heightA} % Scaled height for pA
\pgfmathsetmacro{\scaledHeightB}{\scaleFactor*\heightB} % Scaled height for qB
\pgfmathsetmacro{\scaledHeightC}{\scaleFactor*\heightC} % Scaled height for rB
\pgfmathsetmacro{\scaledHeightD}{\scaleFactor*\heightD} % New scaled height for sA

% Update the bar diagram with proportional scaling
\begin{center}
\begin{tikzpicture}
	% Draw the first set of rectangles (pA + qB)
	\fill[red] (0,0) rectangle (2,\scaledHeightA); % Width doubled
	\fill[blue] (0,\scaledHeightA) rectangle (2,\scaledHeightA+\scaledHeightB); % Width doubled
	\node[anchor=east] at (0,0.5*\scaledHeightA) {\valp A}; % Label for pA
	\node[anchor=east] at (0,\scaledHeightA+0.5*\scaledHeightB) {\valq B};

	% Draw the second set of rectangles (sA + rB) next to the first set with increased spacing
	\fill[red] (4,0) rectangle (6,\scaledHeightD); % New color and width doubled
	\fill[blue] (4,\scaledHeightD) rectangle (6,\scaledHeightD+\scaledHeightC); % Width doubled
	\node[anchor=east] at (4,0.5*\scaledHeightD) {\vals A}; % New label for sA
	\node[anchor=east] at (4,\scaledHeightD+0.5*\scaledHeightC) {\valr B};

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

