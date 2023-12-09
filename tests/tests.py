import unittest
from src.ans import count_values


class TestCountValues(unittest.TestCase):
    def test_count_values(self):
        input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
        expected = {1: 2, 2: 1, 3: 1}
        self.assertEqual(count_values(input_dict), expected)

    def test_count_values_empty(self):
        self.assertEqual(count_values({}), {})

    def test_count_values_same_values(self):
        input_dict = {'a': 1, 'b': 1, 'c': 1}
        expected = {1: 3}
        self.assertEqual(count_values(input_dict), expected)


if __name__ == '__main__':
    unittest.main()
