# day2.py

from utils.utils import * 
from daily.day2a import * #can I do star? seems like it. neato.
from daily.day2b import * 


# # Main program logic
# read the input data (reports)  # Each report is a list of integers

@time_it
def main():
    """Reads the input, processes the data, and prints the results."""
    input = read_integer_lists("../inputs/2-input.txt") 
    
    safe_count = 0
    for report in input:
        if is_report_safe(report):
            safe_count += 1
            
    
    print_solution_box("2a", safe_count)
    
    dampened_safe_count = 0
    for report in input:
        if is_report_safe_with_dampener(report):
            dampened_safe_count += 1
            
    print_solution_box("2b", dampened_safe_count)
    

if __name__ == "__main__":
    main()