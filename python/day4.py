# day4.py

from utils.utils import *
from daily.day4a import *

from daily.day4b import *


@time_it
def main():
    """Reads the input, processes the data, and prints the results."""
    input = read_file_as_lines("../inputs/4-input.txt")

    solution_a = count_xmas_iterative(input)
    solution_b = count_x_mas(input)

    print_solution_box("4a", solution_a)
    print_solution_box("4b", solution_b)


if __name__ == "__main__":
    main()
