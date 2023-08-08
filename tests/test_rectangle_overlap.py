import unittest

from ..src.barebone_poetry_project.solution import Point, Rectangle


class TestRectangleOverlap(unittest.TestCase):
    def test_overlaps_point(self):
        A = Rectangle(bottom_left_point=Point(0, 0), top_right_point=Point(10, 10))
        B = Point(5, 5)
        self.assertEqual(A.overlaps_point(B), True, "Rect Overlaps point")

        A1 = Rectangle(bottom_left_point=Point(0, 0), top_right_point=Point(10, 10))
        B1 = Point(-15, 15)
        self.assertEqual(A.overlaps_point(B), True)
        self.assertEqual(A1.overlaps_point(B1), False)


if __name__ == "__main__":
    unittest.main()
