import unittest
from daily.day1a import calculate_total_distance

class TestDay1a(unittest.TestCase):
  def test_sample_data(self):
    """
    Verifies the calculation using the sample data from the puzzle description.
    """
    pairs = [[3, 4], [4, 3], [2, 5], [1, 3], [3, 9], [3, 3]]
    expected_distance = 11
    self.assertEqual(calculate_total_distance(pairs), expected_distance)

  def test_empty_list(self):
    """Checks the behavior when an empty list of pairs is provided."""
    pairs = []
    expected_distance = 0
    self.assertEqual(calculate_total_distance(pairs), expected_distance)

  def test_single_pair(self):
    pairs = [[5, 2]]
    expected_distance = 3
    self.assertEqual(calculate_total_distance(pairs), expected_distance)

if __name__ == '__main__':
  unittest.main()