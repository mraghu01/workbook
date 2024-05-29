def print_latex_number_line(dividend, divisor):
    unit_length = 10 / dividend
    # LaTeX code for the number line
    latex_code = f"""\\vfill
	\\begin{{tikzpicture}}
    % Draw the number line
    \\draw (0,0) -- ({dividend*unit_length},0);
    % Add the ticks and labels
    \\draw (0,-0.2) -- (0,0.2) node [above] {{0}};
    \\draw ({divisor*10*unit_length},-0.2) -- ({divisor*10*unit_length},0.2) node [above] {{\\small {divisor*10}}};
    \\draw ({dividend*unit_length},-0.2) -- ({dividend*unit_length},0.2) node [above] {{{dividend}}};
\\end{{tikzpicture}}"""
    
    print(latex_code)

# Example usage:
print_latex_number_line(4321, 24)
print_latex_number_line(3780, 36)

