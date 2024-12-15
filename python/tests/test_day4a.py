import unittest
from daily.day4a import *


class TestDay4a(unittest.TestCase):
  
    def test_count_xmas_north(self):
      self.assertEqual(count_xmas_iterative([
          "SXXX",
          "AXXX",
          "MXXX",
          "XXXX",
        ]), 1)
      
    def test_count_xmas_south(self):
      self.assertEqual(count_xmas_iterative([
          "XXXX",
          "MXXX",
          "AXXX",
          "SXXX",
        ]), 1)
      
    def test_count_xmas_east(self):
      self.assertEqual(count_xmas_iterative([
          "XMAS",
          "XXXX",
          "XXXX",
          "XXXX",
        ]), 1)
      
    def test_count_xmas_west(self):
      self.assertEqual(count_xmas_iterative([
          "SAMX",
          "XXXX",
          "XXXX",
          "XXXX",
        ]), 1)
      
    def test_count_xmas_northeast(self):
      self.assertEqual(count_xmas_iterative([
          "XXXS",
          "XXAX",
          "XMXX",
          "XXXX",
        ]), 1)
    def test_count_xmas_northwest(self):
      self.assertEqual(count_xmas_iterative([
          "SXXX",
          "XAXX",
          "XXMX",
          "XXXX",
        ]), 1)
    def test_count_xmas_southeast(self):
      self.assertEqual(count_xmas_iterative([
          "XXXX",
          "XMXX",
          "XXAX",
          "XXXS",
        ]), 1)
    def test_count_xmas_southwest(self):
      self.assertEqual(count_xmas_iterative([
          "XXXX",
          "XXMX",
          "XAXX",
          "SXXX",
        ]), 1)
    def test_count_xmas_two_overlapping(self):
      self.assertEqual(count_xmas_iterative([
          "XXXX",
          "XXMM",
          "XAXA",
          "SXXS",
        ]), 2)
    def test_count_xmas_iterative(self):
        self.assertEqual(count_xmas_iterative([
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX",
        ]), 18)

    def test_count_xmas_iterative_alternate(self):
        self.assertEqual(count_xmas_iterative([
            "....XXMAS.",
            ".SAMXMS...",
            "...S..A...",
            "..A.A.MS.X",
            "XMASAMX.MM",
            "X.....XA.A",
            "S.S.S.S.SS",
            ".A.A.A.A.A",
            "..M.M.M.MM",
            ".X.X.XMASX",
        ]), 18)

    def test_count_xmas_iterative_shorter(self):
      self.assertEqual(count_xmas_iterative([
          "XMAS",
          "MASX",
          "ASXM",
          "SXMA",
      ]), 2)

    def test_count_xmas_iterative_find_none(self):
      self.assertEqual(count_xmas_iterative([
          "XXXX",
          "XXXX",
          "XXXX",
          "XXXX",
      ]), 0)


    def test_count_xmas_iterative_overlapping(self):
      self.assertEqual(count_xmas_iterative([
          "XMASXMAS",
          "XMASXMAS",
          "XMASXMAS",
          "XMASXMAS",
      ]), 12)  # Overlapping matches


if __name__ == "__main__":
    unittest.main()
