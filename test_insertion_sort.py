import random
import unittest

from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def test_empty_list(self):
        result, _ = insertion_sort([])
        self.assertEqual(result, [])

    def test_single_element(self):
        result, _ = insertion_sort([42])
        self.assertEqual(result, [42])

    def test_already_sorted(self):
        data = [1, 2, 3, 4, 5]
        result, _ = insertion_sort(data)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        data = [5, 4, 3, 2, 1]
        result, _ = insertion_sort(data)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_duplicates(self):
        data = [3, 1, 2, 3, 1]
        result, _ = insertion_sort(data)
        self.assertEqual(result, [1, 1, 2, 3, 3])

    def test_negative_numbers(self):
        data = [-5, 3, -1, 0, 2]
        result, _ = insertion_sort(data)
        self.assertEqual(result, [-5, -1, 0, 2, 3])

    def test_random_matches_builtin_sorted(self):
        data = [random.randint(-1000, 1000) for _ in range(200)]
        result, _ = insertion_sort(data)
        self.assertEqual(result, sorted(data))

    def test_does_not_mutate_input(self):
        data = [3, 1, 2]
        original = data.copy()
        insertion_sort(data)
        self.assertEqual(data, original)

    def test_returns_process_time(self):
        _, process_time = insertion_sort([3, 1, 2])
        self.assertIsInstance(process_time, float)
        self.assertGreaterEqual(process_time, 0)


if __name__ == "__main__":
    unittest.main()
