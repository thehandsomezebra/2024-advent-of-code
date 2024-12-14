def read_integer_lists(filename):
  """
  Reads a file containing lists of integers and returns a list of lists.

  Each line in the file is treated as a separate list of integers.

  Args:
    filename: The name of the input file.

  Returns:
    A list of lists of integers.
  """
  with open(filename, "r") as f:
    lists = [[int(num) for num in line.strip().split()] for line in f]
  return lists