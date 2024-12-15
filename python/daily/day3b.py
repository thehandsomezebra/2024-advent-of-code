import re
def calculate_total_with_conditions(input_string):
    solution = 0
    enabled = True
    for i in range(len(input_string)):
        if input_string[i:].startswith("do()"):
            enabled = True
        if input_string[i:].startswith("don't()"):
            enabled = False
        instr = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", input_string[i:])
        if instr is not None:
            x, y = int(instr.group(1)), int(instr.group(2))
            if enabled:
                solution += x * y
    return solution
