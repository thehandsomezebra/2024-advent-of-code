# day2.py

from day2a import * #can I do star? seems like it. neato.
# from day2b import thing 
from utils import read_input 

# # Main program logic
# read the input data (reports)  # Each report is a list of integers

def main():
    """Reads the input, processes the data, and prints the results."""
    safe_count = 0
    input = read_input("inputs/2-input.txt") 

    for report in input:
        if is_report_safe(report):
            safe_count += 1
    # print(safe_count)

    # total_distance = calculate_total_distance(input)
    print("Advent of Code 2024 Day 2a Solution....")
    print("+-----------------------------------+")
    print("|       Safe Count: ", safe_count,"           |")
    print("+-----------------------------------+")

    # blah = thing(input)
    # print("Advent of Code 2024 Day 2b Solution....")
    # print("+-----------------------------------+")
    # print("|       whatever Score: ", thing," |")
    # print("+-----------------------------------+")


if __name__ == "__main__":
    main()