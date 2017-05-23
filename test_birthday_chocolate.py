import birthday_chocolate
import unittest

VALUE_ONE = [5, [1, 2, 1, 3, 2], 3, 2, 2]
VALUE_TWO = [6, [1, 1, 1, 1, 1, 1], 3, 2, 0]
VALUE_THREE = [1, [4], 4, 1, 1]
TEST_COLLECTION = [VALUE_TWO, VALUE_THREE, VALUE_ONE]


class BirthdayChocolateTest(unittest.TestCase):

    def setUp(self):
        self.calculator = birthday_chocolate.BirthdayChocolate()

    def test_solve(self):
        for values in TEST_COLLECTION:
            self.assertEqual(values[4], self.calculator.solve(values[0], values[1], values[2], values[3]))

    def test_check_constraint(self):
        self.assertFalse(self.calculator.check_constraints(0, [4], 4, 1))
        self.assertFalse(self.calculator.check_constraints(1, [6], 4, 1))
        self.assertFalse(self.calculator.check_constraints(1, [4], 32, 1))
        self.assertFalse(self.calculator.check_constraints(1, [4], 4, 13))
        self.assertTrue(self.calculator.check_constraints(1, [4], 4, 1))
