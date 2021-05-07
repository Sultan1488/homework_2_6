import unittest
from home_code_2_6_1 import calculate_average_velocity


class TestHomeCode2_6_1(unittest.TestCase):
    def test_result(self):
        self.assertEqual(calculate_average_velocity(321, 213, 432), 322.0)
        self.assertEqual(calculate_average_velocity(1, 2, 3), 2.0)
        self.assertEqual(calculate_average_velocity(56, 34, 66), 52.0)

    def test_alpha_returns_zero(self):
        self.assertEqual(calculate_average_velocity('123'), 0)

    def test_result_float(self):
        self.assertIsInstance(calculate_average_velocity(52.0), float)


unittest.main()
