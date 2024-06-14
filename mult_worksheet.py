import random

# Provided function from the file "mult_worksheet.py"
def create_multiplication_steps():
    # Generate a random 3-digit and a 2-digit number
    three_digit_number = random.randint(100, 999)
    two_digit_number = random.randint(10, 99)

    # Round the numbers to the nearest hundred and ten
    rounded_three_digit = round(three_digit_number, -2)
    rounded_two_digit = round(two_digit_number, -1)

    # Calculate the steps
    steps = [
        (rounded_three_digit, rounded_two_digit),
        (round(three_digit_number, -1), rounded_two_digit),
        (three_digit_number, rounded_two_digit),
        (three_digit_number, two_digit_number)
    ]

    # Remove duplicate steps
    unique_steps = []
    for step in steps:
        if not unique_steps or step != unique_steps[-1]:
            unique_steps.append(step)

    # Return the unique steps as a string
    return ' \\\\\\\\ '.join(f"${step[0]} \\times {step[1]} = \\_\\_\\_\\_$" for step in unique_steps)

# Function to generate LaTeX code for the table
def generate_latex_table():
    latex_code = "\\documentclass[letterpaper,12pt]{article}\n"
    latex_code += "\\usepackage{array}\n"
    latex_code += "\\begin{document}\n"
    latex_code += "\\begin{tabular}{|>{\\centering\\arraybackslash}m{0.5\\textwidth}|>{\\centering\\arraybackslash}m{0.5\\textwidth}|}\n"
    latex_code += "\\hline\n"
    for _ in range(3):
        latex_code += f"\\begin{{minipage}}{{0.5\\textwidth}}\n{create_multiplication_steps()}\\\\\n\\end{{minipage}} & "
        latex_code += f"\\begin{{minipage}}{{0.5\\textwidth}}\n{create_multiplication_steps()}\\\\\n\\end{{minipage}} \\\\\n\\hline\n"
    latex_code += "\\end{tabular}\n"
    latex_code += "\\end{document}\n"
    return latex_code

# Print the LaTeX code
print(generate_latex_table())

