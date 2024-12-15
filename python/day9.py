# day9.py

from utils.utils import *
from daily.day9a import *
# from daily.day9b import *


@time_it
def main():
    """Reads the input, processes the data, and prints the results."""
    input = read_integer_lists("../inputs/9-input.txt")


    solution_a = thinga(input)
    solution_b = thingb(input)

    print_solution_box("9a", solution_a)
    print_solution_box("9b", solution_b)


if __name__ == "__main__":
    main()
