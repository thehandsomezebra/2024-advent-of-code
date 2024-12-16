# day6.py

from utils.utils import *
from daily.day6a import *
# from daily.day6b import *


@time_it
def main():
    """Reads the input, processes the data, and prints the results."""
    input = read_file_as_lines("../inputs/6-input.txt")

    solution_a = simulate_guard_path(input)
    # solution_b = thingb(input)

    print_solution_box("6a", solution_a)
    # print_solution_box("6b", solution_b)

if __name__ == "__main__":
    main()
