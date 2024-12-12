def is_report_safe(report):
  # RULE ONE: The difference between levels must be between 1 and 3
  # Check if the report is empty or has only one level
  # print("length of report", len(report)) # I want to see the length, to make sure I'm doing this part right
  if len(report) < 2:
    return True

# RULE TWO: The levels must be increasing or decreasing.. Not a mix.
  # Determine if the report should be increasing or decreasing
  is_increasing = report[1] > report[0]  # Compare the first two levels to set a direction


  # Iterate through the levels using zip to check pairs
  for this_level, that_level in zip(report, report[1:]):  
      #I used zip in day 1, cool. 
      #The other interesting thing with the report[1:] is that it's a slice of the list, starting at the second element. simple.
      
    # Check the difference
    if not 1 <= abs(this_level - that_level) <= 3:  
      #abs is cool, it's gunna return the absolute value.. so if it's negative, it'll make it positive.
      
      return False

    # Check increasing/decreasing
    if is_increasing and this_level >= that_level:  
      return False
    if not is_increasing and this_level <= that_level:  
      return False

  return True  # Safe if all checks pass

# # Main program logic
# read the input data (reports)  # Each report is a list of integers
safe_count = 0
test_reports = [
    [7, 6, 4, 2, 1],  # Safe (decreasing)
    [1, 2, 7, 8, 9],  # Unsafe (increase of 5)
    [9, 7, 6, 2, 1],  # Unsafe (decrease of 4)
    [1, 3, 2, 4, 5],  # Unsafe (increasing then decreasing)
    [8, 6, 4, 4, 1],  # Unsafe (no change)
    [1, 3, 6, 7, 9]   # Safe (increasing)
]


# test_reports = [
#     [7, 6, 4, 2, 1]  # Safe (decreasing)
# ]
for report in test_reports:
  if is_report_safe(report):
    safe_count += 1
print(safe_count)