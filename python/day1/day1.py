# day1.py

from day1a import calculate_total_distance 
from day1b import calculate_similarity_score 
from utils import read_input 

def main():
    """Reads the input, processes the data, and prints the results."""
    input = read_input("inputs/1-input.txt") 

    total_distance = calculate_total_distance(input)
    print("Advent of Code 2024 Day 1a Solution....")
    print("+-----------------------------------+")
    print("|       Total Difference: ", total_distance," |")
    print("+-----------------------------------+")

    similarity_score = calculate_similarity_score(input)
    print("Advent of Code 2024 Day 1b Solution....")
    print("+-----------------------------------+")
    print("|       Similarity Score: ", similarity_score," |")
    print("+-----------------------------------+")


if __name__ == "__main__":
    main()