# day2.py

from utils.utils import read_integer_lists 
from daily.day2a import * #can I do star? seems like it. neato.
from daily.day2b import * 


# # Main program logic
# read the input data (reports)  # Each report is a list of integers

def main():
    """Reads the input, processes the data, and prints the results."""
    safe_count = 0
    input = read_integer_lists("../inputs/2-input.txt") 

    for report in input:
        if is_report_safe(report):
            safe_count += 1
            
            
    print("Advent of Code 2024 Day 2a Solution....")
    print("+-----------------------------------+")
    print("|       Safe Count: ", safe_count,"           |")
    print("+-----------------------------------+")

    dampened_safe_count = 0
    for report in input:
        if is_report_safe_with_dampener(report):
            dampened_safe_count += 1
            
    print("Advent of Code 2024 Day 2b Solution....")
    print("+-----------------------------------+")
    print("|  Safe Count with Dampener: ", dampened_safe_count," |")
    print("+-----------------------------------+")


if __name__ == "__main__":
    main()