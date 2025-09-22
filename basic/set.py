import unittest

class TestSet(unittest.TestCase):
    def test_set_curly(self):
        self.assertEqual({"apple", "banana", "orange", "banana"}, {"apple", "banana", "orange"})

    def test_set_fn(self):
        self.assertEqual(set(["apple", "banana", "orange", "banana"]), {"apple", "banana", "orange"})

    def test_set_add(self):
        fruits = set(["apple", "banana", "orange", "banana"])
        fruits.add('melon')
        self.assertEqual(fruits, {"apple", "banana", "orange", "melon"})

    def test_set_remove(self):
        fruits = set(["apple", "banana", "orange", "banana"])
        fruits.remove('orange')
        self.assertEqual(fruits, {"apple", "banana"})

    def test_set_remove_invalid(self):
        fruits = set(["apple", "banana", "orange", "banana"])
        with self.assertRaises(KeyError):
            fruits.remove('melon')

    def test_set_discard(self):
        fruits = set(["apple", "banana", "orange", "banana"])
        fruits.discard('orange')
        self.assertEqual(fruits, {"apple", "banana"})

    def test_set_discard_invalid(self):
        fruits = set(["apple", "banana", "orange", "banana"])
        fruits.discard('melon')

    def test_set_union(self):
        fruits1 = set(["apple", "banana"])
        fruits2 = set(["grape", "melon"])
        self.assertEqual(fruits1 | fruits2, {"apple", "banana", "grape", "melon"})

    def test_set_union_fn(self):
        fruits1 = set(["apple", "banana"])
        fruits2 = set(["grape", "melon"])
        self.assertEqual(fruits1.union(fruits2), {"apple", "banana", "grape", "melon"})

    def test_set_intersection(self):
        fruits1 = set(["apple", "banana", "orange", "melon"])
        fruits2 = set(["grape", "banana", "melon", "pear"])
        self.assertEqual(fruits1 & fruits2, {"banana", "melon"})

    def test_set_intersection_fn(self):
        fruits1 = set(["apple", "banana", "orange", "melon"])
        fruits2 = set(["grape", "banana", "melon", "pear"])
        self.assertEqual(fruits1.intersection(fruits2), {"banana", "melon"})

    def test_set_difference(self):
        fruits1 = set(["apple", "banana", "orange", "melon"])
        fruits2 = set(["grape", "banana", "melon", "pear"])
        self.assertEqual(fruits1 - fruits2, {"apple", "orange"})

    def test_set_difference_fn(self):
        fruits1 = set(["apple", "banana", "orange", "melon"])
        fruits2 = set(["grape", "banana", "melon", "pear"])
        self.assertEqual(fruits1.difference(fruits2), {"apple", "orange"})

    def test_set_issubset(self):
        fruits1 = set(["apple", "banana"])
        fruits2 = set(["apple", "banana", "melon", "orange"])
        self.assertTrue(fruits1 <= fruits2)

    def test_set_issubset_fn(self):
        fruits1 = set(["apple", "banana"])
        fruits2 = set(["grape", "banana", "melon", "pear"])
        self.assertFalse(fruits1.issubset(fruits2))

    def test_set_issuperset(self):
        fruits1 = set(["apple", "banana", "melon", "orange"])
        fruits2 = set(["apple", "banana"])
        self.assertTrue(fruits1 >= fruits2)

    def test_set_issuperset_fn(self):
        fruits1 = set(["grape", "banana", "melon", "pear"])
        fruits2 = set(["apple", "banana"])
        self.assertFalse(fruits1.issuperset(fruits2))

    def test_set_value_exist(self):
        fruits = set(["apple", "banana", "orange", "melon"])
        self.assertIn('apple', fruits)
        self.assertNotIn('pear', fruits)

if __name__ == '__main__':
    unittest.main()
