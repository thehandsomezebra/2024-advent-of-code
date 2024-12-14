import unittest
from daily.day1b import calculate_similarity_score  

class TestDay1b(unittest.TestCase):
    def test_sample_data(self):
        """Verifies the calculation using the sample data from the puzzle description."""
        pairs = [[3, 4], [4, 3], [2, 5], [1, 3], [3, 9], [3, 3]]
        expected_score = 31
        self.assertEqual(calculate_similarity_score(pairs), expected_score)

    def test_empty_list(self):
        """Checks the behavior when an empty list of pairs is provided."""
        pairs = []
        expected_score = 0
        self.assertEqual(calculate_similarity_score(pairs), expected_score)

    def test_no_matches(self):
        """Checks when no numbers from the left list appear in the right list."""
        pairs = [[1, 2], [3, 4], [5, 6]]
        expected_score = 0
        self.assertEqual(calculate_similarity_score(pairs), expected_score)

    def test_all_matches(self):
        """Checks when all numbers from the left list appear in the right list."""
        pairs = [[1, 1], [2, 2], [3, 3]]
        expected_score = 6  # 1*1 + 2*1 + 3*1 = 6
        self.assertEqual(calculate_similarity_score(pairs), expected_score)

if __name__ == '__main__':
    unittest.main()