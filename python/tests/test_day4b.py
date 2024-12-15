import unittest
from daily.day4b import count_x_mas  # Make sure to import your function correctly


class TestCountXMas(unittest.TestCase):
    def test_count_x_mas(self):
        self.assertEqual(
            count_x_mas(
                [
                    ".M.S......",
                    "..A..MSMS.",
                    ".M.S.MAA..",
                    "..A.ASMSM.",
                    ".M.S.M....",
                    "..........",
                    "S.S.S.S.S.",
                    ".A.A.A.A..",
                    "M.M.M.M.M.",
                    "..........",
                ]
            ),
            9,
        )  # Example from problem description

        self.assertEqual(
            count_x_mas(
                [
                    "MMM",
                    "AAA",
                    "SMS",
                ]
            ),
            1,
        )  # Single X-MAS

        self.assertEqual(
            count_x_mas(
                [
                    "AAA",
                    "AAA",
                    "AAA",
                ]
            ),
            0,
        )  # No X-MAS

        self.assertEqual(
            count_x_mas(
                [
                    "MMMMS",
                    "AAAAA",
                    "SSSSS",
                ]
            ),
            2,
        )  # Two overlapping X-MAS


if __name__ == "__main__":
    unittest.main()
