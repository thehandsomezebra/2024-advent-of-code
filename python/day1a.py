def calculate_total_distance(pairs):
#   """Calculates the total distance between pairs of numbers.

#   Args:
#     pairs: A list of lists, where each inner list represents a pair of numbers.

#   Returns:
#     The total distance between the pairs.
#   """
  left_list = sorted([pair[0] for pair in pairs])
  right_list = sorted([pair[1] for pair in pairs])
  total_distance = 0

  for left, right in zip(left_list, right_list):
    total_distance += abs(left - right)

  return total_distance

# Example usage with the provided sample data:
# pairs = [[3, 4], [4, 3], [2, 5], [1, 3], [3, 9], [3, 3]]
# distance = calculate_total_distance(pairs)
# print(f"Total distance: {distance}")  # Output: Total distance: 11
# print(calculate_total_distance.__doc__)  # Output: Show to documentation of the function