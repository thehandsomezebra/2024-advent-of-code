# day3.py

from daily.day3a import *
from daily.day3b import *

from utils.utils import *

@time_it
def main():
    """Reads the input, processes the data, and prints the results."""
    input = read_file_as_string("../inputs/3-input.txt")

    solution_a = calculate_total_multiplications(input)
    solution_b = calculate_total_with_conditions(input)

    print_solution_box("3a", solution_a)
    print_solution_box("3b", solution_b)

if __name__ == "__main__":
    main()
