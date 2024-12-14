import unittest
from daily.day2a import validate_level_differences, validate_increasing_or_decreasing, is_report_safe


# so the difference that I'm doing for day 2 vs day 1 is that I'm doing lots of assertions under one test..
# Day 1, I just did one assertion per test.
# I don't think I need to do hard isolations like I did for day 1.. 
# Either way is fine, I guess better to separate things out when the complexity increases. amirite?
class TestDay2a(unittest.TestCase):
    def test_validate_level_differences(self):
        self.assertTrue(validate_level_differences([1, 2, 3, 4]))
        self.assertTrue(validate_level_differences([4, 3, 2, 1]))
        self.assertTrue(validate_level_differences([1, 2, 5, 6]))  # Difference of 3, still good
        self.assertFalse(validate_level_differences([1, 5, 2, 6]))  # Difference of 4, this is bad
        self.assertTrue(validate_level_differences([1]))  # Single element
        self.assertTrue(validate_level_differences([]))  # Empty list

    def test_validate_increasing_or_decreasing(self):
        self.assertTrue(validate_increasing_or_decreasing([1, 2, 3, 4]))
        self.assertTrue(validate_increasing_or_decreasing([4, 3, 2, 1]))
        self.assertFalse(validate_increasing_or_decreasing([1, 3, 2, 4]))  # Not strictly increasing/decreasing
        self.assertFalse(validate_increasing_or_decreasing([1, 2, 2, 3]))  # Not strictly increasing
        self.assertTrue(validate_increasing_or_decreasing([1]))  # Single element
        self.assertTrue(validate_increasing_or_decreasing([]))  # Empty list

    def test_is_report_safe(self):
        self.assertTrue(is_report_safe([1, 2, 3, 4]))
        self.assertTrue(is_report_safe([4, 3, 2, 1]))
        self.assertFalse(is_report_safe([1, 2, 5, 9]))  # Fails level difference rule
        self.assertFalse(is_report_safe([1, 3, 2, 4]))  # Fails increasing/decreasing rule
        self.assertTrue(is_report_safe([1]))  # Single element
        self.assertTrue(is_report_safe([]))  # Empty list

if __name__ == '__main__':
    unittest.main()