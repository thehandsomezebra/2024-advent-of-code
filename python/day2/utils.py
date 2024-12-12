def read_input(filename):
  """Reads the input file and returns a list of pairs.

  Args:
    filename: The name of the input file.

  Returns:
    A list of lists, where each inner list represents a pair of numbers.
  """
  with open(filename, "r") as f:
    pairs = [[int(num) for num in line.strip().split()] for line in f]
  return pairs