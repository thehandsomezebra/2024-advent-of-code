# day1.py

from utils.utils import * 
from daily.day1a import calculate_total_distance 
from daily.day1b import calculate_similarity_score 


@time_it
def main():
    """Reads the input, processes the data, and prints the results."""
    input = read_integer_lists("../inputs/1-input.txt") 

    total_distance = calculate_total_distance(input)
    print_solution_box("1a", total_distance)

    similarity_score = calculate_similarity_score(input)
    print_solution_box("1b", similarity_score)


if __name__ == "__main__":
    main()