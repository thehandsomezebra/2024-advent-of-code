# daily.day1b.py 

def calculate_similarity_score(pairs):
    """Calculates the similarity score between two lists of numbers.

    Args:
      pairs: A list of lists, where each inner list represents a pair of numbers.

    Returns:
      The similarity score between the lists.
    """
    #   grab column 0 and column 1 from pairs
    left_list = [pair[0] for pair in pairs]
    right_list = [pair[1] for pair in pairs]
    similarity_score = 0

    for left_num in left_list:
        # Count occurrences in the right list
        # https://docs.python.org/3/library/array.html#array.array.count
        count = right_list.count(left_num)
        similarity_score += left_num * count

    return similarity_score
