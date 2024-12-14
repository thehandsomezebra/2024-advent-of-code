# daily.day2a.py 

def validate_level_differences(report):
  # RULE ONE: The difference between levels must be between 1 and 3
  """Checks if the differences between adjacent levels are within the allowed range (1 to 3)."""
  for this_level, that_level in zip(report, report[1:]):
      #I used zip in day 1, cool. 
      #The other interesting thing with the report[1:] is that it's a slice of the list, starting at the second element. simple.
      #abs is cool, it's gunna return the absolute value.. so if it's negative, it'll make it positive.
    if not 1 <= abs(this_level - that_level) <= 3:
      return False  # Not safe
  return True  # Safe if all differences are valid
  



def validate_increasing_or_decreasing(report):
  """Checks if the levels are strictly increasing or strictly decreasing."""
  # RULE TWO: The levels must be increasing or decreasing.. Not a mix.
  # Start by checking if the report is empty or has only one level
  if len(report) < 2:
    return True
  
  # Determine if the report should be increasing or decreasing
  is_increasing = report[1] > report[0]  # Compare the first two levels to set a direction

  # Iterate through the levels using zip to check pairs
  for this_level, that_level in zip(report, report[1:]):
    if is_increasing and this_level >= that_level:
      return False
    if not is_increasing and this_level <= that_level:
      return False
  return True  # Valid if strictly increasing or decreasing

def is_report_safe(report):
  """Checks if a report is safe based on both rules."""
  return validate_level_differences(report) and validate_increasing_or_decreasing(report)
