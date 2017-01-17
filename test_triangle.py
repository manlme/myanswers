import unittest
from triangle import tell_triangle
class TestTriangle(unittest.TestCase):
    def testTriangles(self):
        self.assertEqual("equilateral", tell_triangle(3,3,3))
        self.assertEqual('isosceles', tell_triangle(3,3,2))
        self.assertEqual('scalene', tell_triangle(3,2,4))
        self.assertEqual('not a triangle', tell_triangle(1, -1, 1))
        self.assertEqual('not a triangle', tell_triangle(1,2,3))
if __name__ == '__main__':
    unittest.main()
