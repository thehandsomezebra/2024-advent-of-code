# day7.py

from utils.utils import *
from daily.day7a import *
# from daily.day7b import *


@time_it
def main():
    """Reads the input, processes the data, and prints the results."""
    input = read_integer_lists("../inputs/7-input.txt")


    solution_a = thinga(input)
    solution_b = thingb(input)
    
    print_solution_box("7a", solution_a)
    print_solution_box("7b", solution_b)


if __name__ == "__main__":
    main()
