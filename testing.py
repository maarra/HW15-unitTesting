import unittest

class TestIntegerSet(unittest.TestCase):
    def setUp(self):
        self.empty_set = IntegerSet()
        self.single_element_set = IntegerSet([42])
        self.multiple_elements_set = IntegerSet([1, 2, 3, 4, 5])

    def test_sum(self):
        self.assertEqual(self.empty_set.sum(), 0)
        self.assertEqual(self.single_element_set.sum(), 42)
        self.assertEqual(self.multiple_elements_set.sum(), 15)

    def test_mean(self):
        self.assertEqual(self.empty_set.mean(), 0)
        self.assertEqual(self.single_element_set.mean(), 42)
        self.assertAlmostEqual(self.multiple_elements_set.mean(), 3)

    def test_max(self):
        self.assertIsNone(self.empty_set.max())
        self.assertEqual(self.single_element_set.max(), 42)
        self.assertEqual(self.multiple_elements_set.max(), 5)

    def test_min(self):
        self.assertIsNone(self.empty_set.min())
        self.assertEqual(self.single_element_set.min(), 42)
        self.assertEqual(self.multiple_elements_set.min(), 1)

    def test_add(self):
        self.empty_set.add(10)
        self.assertIn(10, self.empty_set.integers)
        self.empty_set.add(20)
        self.assertIn(20, self.empty_set.integers)
        self.single_element_set.add(10)
        self.assertIn(10, self.single_element_set.integers)

if __name__ == "__main__":
    unittest.main()