import unittest
import calc

class TestCalcMethod(unittest.TestCase):

    def test_addition(self):
        tests = [(0, 0, 0), (1, 1, 2), (45636, 3563, 49199)]
        self.assertTrue(all([calc.addition(x, y) == a for x,y,a in tests]))

    def test_addition_fail(self):
        self.assertRaises(TypeError, calc.addition, args=("48958", 5))

    def test_subtraction(self):
        tests = [(0, 0, 0), (1, 2, -1), (100, 20, 80)]
        self.assertTrue(all([calc.subtraction(x, y) == a for x,y,a in tests]))

    def test_subtraction_fail(self):
        self.assertRaises(TypeError, calc.subtraction, args=("48958", 5))

    def test_division(self):
        tests = [(1, 1, 1), (15, 15, 1), (1, 0, None)]
        for x,y,a in tests:
            self.assertAlmostEqual(calc.division(x, y), a)

    def test_division_fail(self):
        self.assertRaises(TypeError, calc.division, args=("48958", 5))

    def test_multiplication(self):
        tests = [(1, 1, 1), (2, 2, 4), (45636, 3563, 162601068)]
        self.assertTrue(all([calc.multiplication(x, y) == a for x,y,a in tests]))

    def test_multiplication_fail(self):
        self.assertRaises(TypeError, calc.multiplication, args=("48958", 5))

if __name__ == "__main__":
    unittest.main()
