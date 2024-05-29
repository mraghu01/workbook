import random

def generate_division_row(divisor_range, dividend_range):
    # Ensure the divisor is less than 10 and not zero
    divisor = random.choice(divisor_range)
    
    # Generate a random dividend that is evenly divisible by the divisor
    dividend = random.choice(dividend_range)
    
    # Round the dividend to the nearest 10 that is still divisible by the divisor
    rounded_dividend = round(dividend, -1)
    while rounded_dividend % divisor != 0:
        rounded_dividend -= 10
    
    # Calculate the difference
    difference = abs(dividend - rounded_dividend)
    
    # Create the LaTeX row
    latex_row = f"\\huge ${dividend} \\div {divisor}=$ \\raisebox{{-0.25\\height}}{{\\colorbox{{blue!30}}{{\\rule{{0pt}}{{40pt}}\\hspace{{3em}}}}}} & \\huge ${rounded_dividend} \\div {divisor}=$ \\raisebox{{-0.25\\height}}{{\\colorbox{{blue!30}}{{\\rule{{0pt}}{{40pt}}\\hspace{{3em}}}}}} & \\huge ${difference} \\div {divisor}=$ \\raisebox{{-0.25\\height}}{{\\colorbox{{blue!30}}{{\\rule{{0pt}}{{40pt}}\\hspace{{3em}}}}}} \\\\ [\\rowheight] \\hline"
    
    return latex_row



docheader = '''
\\documentclass{article}
\\pagestyle{empty}
\\usepackage[letterpaper, margin=0.5in]{geometry} % Set page to letter size with 0.5-inch margins
\\usepackage{array} % For better table control
\\usepackage{amsmath} % For math symbols and environments
\\usepackage{xcolor} % For colored boxes

\\newlength{\\rowheight} % Define a new length for row height
\\setlength{\\rowheight}{48pt} % Set the initial value of row height

\\begin{document}
'''


print(docheader)

tableheader = '''
\\begin{table}[h!]
\\centering
\\setlength{\\arrayrulewidth}{1mm} % Set the thickness of the border
\\setlength{\\extrarowheight}{\\dimexpr(\\textheight-5\\arrayrulewidth-10\\tabcolsep)/10-2\\arrayrulewidth\\relax} % Adjust row height for 5 rows
\\begin{tabular}{|m{0.3\\linewidth}|m{0.3\\linewidth}|m{0.3\\linewidth}|}
\\hline
'''

print(tableheader)

# Define the range for divisors and dividends
divisor_range = list(range(6, 13))
dividend_range = list(range(200, 2000))

# Generate 5 random rows
for _ in range(5):
    print(generate_division_row(divisor_range, dividend_range))

trailer = '''
\\end{tabular}
\\end{table}

\\end{document}
'''

print(trailer)


