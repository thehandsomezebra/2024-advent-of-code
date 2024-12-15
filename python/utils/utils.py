
import shutil
import time


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

def read_file_as_string(filename):
  """Reads an entire file and returns its contents as a single string.

  Args:
    filename: The name of the input file.

  Returns:
    The contents of the file as a single string.
  """
  with open(filename, "r") as f:
    file_content = f.read()
  return file_content

def read_file_as_lines(filename):
  """Reads a file and returns a list of lines with trailing newlines removed.

  Args:
    filename: The name of the input file.

  Returns:
    A list of strings, where each string is a line from the file.
  """
  with open(filename, "r") as f:
    lines = [line.rstrip("\n") for line in f]  # Remove trailing newlines
  return lines

def print_solution_box(day, solution):
  """Prints the solution in a dynamically sized box.

  Args:
    day: The day of the Advent of Code challenge (e.g., "1a", "2b").
    solution: The solution to the challenge.
  """
  terminal_width = shutil.get_terminal_size().columns
  box_width = min(terminal_width - 4, 40)  # Adjust 40 to your preferred max width
  
  # Calculate padding with adjustment for odd lengths
  # lol, this makes me happy.. reminds me of the days when I'd have to 
  # mark out my output on paper templates and count the spaces.. but better
  padding = box_width - len(str(solution)) - 4  # Total padding needed
  left_padding = padding // 2
  right_padding = padding - left_padding  # Adjust for odd lengths

  print(f"Advent of Code 2024 Day {day} Solution....")
  print("+" + "-" * box_width + "+")
  print("|  " + " " * left_padding + str(solution) + " " * right_padding + "  |")
  print("+" + "-" * box_width + "+")


def time_it(func):
  """Decorator to measure the execution time of a function.

  Args:
    func: The function to be timed.

  Returns:
    A wrapper function that times the execution of the decorated function.
  """
  def wrapper(*args, **kwargs):
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"...... execution time: {elapsed_time:.2f} seconds ......")
    # Gives seconds to 2 decimal places
    
    return result
  return wrapper