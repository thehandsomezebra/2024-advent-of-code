# daily.day1a.py 

def calculate_total_distance(pairs):
  """Calculates the total distance between pairs of numbers.

  Args:
    pairs: A list of lists, where each inner list represents a pair of numbers.

  Returns:
    The total distance between the pairs.
  """
  left_list = sorted([pair[0] for pair in pairs])
  right_list = sorted([pair[1] for pair in pairs])
  total_distance = 0

  # zip combines elements from left_list and right_list into pairs
  # https://docs.python.org/3/library/functions.html#zip
  for left, right in zip(left_list, right_list):
    total_distance += abs(left - right)

  return total_distance
