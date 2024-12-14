import unittest
from daily.day2b import *




class TestDay2b(unittest.TestCase):
    def test_is_report_safe_with_dampener(self):
        self.assertTrue(is_report_safe_with_dampener([7, 6, 4, 2, 1]))  # Safe without removing any level
        self.assertFalse(is_report_safe_with_dampener([1, 2, 7, 8, 9]))  # Unsafe regardless of removal
        self.assertFalse(is_report_safe_with_dampener([9, 7, 6, 2, 1]))  # Unsafe regardless of removal
        self.assertTrue(is_report_safe_with_dampener([1, 3, 2, 4, 5]))  # Safe by removing 3
        self.assertTrue(is_report_safe_with_dampener([8, 6, 4, 4, 1]))  # Safe by removing the third 4
        self.assertTrue(is_report_safe_with_dampener([1, 3, 6, 7, 9]))  # Safe without removing any level
        self.assertTrue(is_report_safe_with_dampener([1, 3, 2, 5, 6]))  # Another simple one
        self.assertTrue(is_report_safe_with_dampener([5, 4, 5, 6, 7, 8]))  # Down, then up.. But you have to ignore the first digit
        self.assertTrue(is_report_safe_with_dampener([1, 6, 7, 8, 9]))  # 1 skips 5.. but the others are safe
        



if __name__ == '__main__':
    unittest.main()