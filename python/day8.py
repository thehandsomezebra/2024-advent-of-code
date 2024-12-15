# day8.py

from utils.utils import *
from daily.day8a import *
# from daily.day8b import *


@time_it
def main():
    """Reads the input, processes the data, and prints the results."""
    input = read_integer_lists("../inputs/8-input.txt")


    solution_a = thinga(input)
    solution_b = thingb(input)

    print_solution_box("8a", solution_a)
    print_solution_box("8b", solution_b)


if __name__ == "__main__":
    main()
