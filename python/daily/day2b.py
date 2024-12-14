# daily.day2b.py 

from daily.day2a import * 

def is_report_safe_with_dampener(report):
  """Checks if a report is safe, considering the Problem Dampener."""

#Run the regular check first
  if is_report_safe(report):
    return True

#and now use a list slice to go through the report and remove each level one at a time to see if it's safe.
  for i in range(len(report)):
    modified_report = report[:i] + report[i+1:]  # Remove the i-th level
    if is_report_safe(modified_report):
      return True

  return False
