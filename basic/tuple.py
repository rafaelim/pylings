import unittest

class TestTuples(unittest.TestCase):
    def test_tuple(self):
        fruits = ('apple', 'banana', 'orange')
        self.assertEqual(fruits[0], 'apple')

    def test_tuple_immutability(self):
        fruits = ('apple', 'banana', 'orange')
        with self.assertRaises(TypeError):
            # This operation is not allowed on tuples.
            fruits[1] = 'grape'

    def test_tuple_concatenation(self):
        fruits1 = ('apple', 'banana')
        fruits2 = ('orange', 'grape')
        new_tuple = fruits1 + fruits2
        # Verify the new tuple contains all the elements.
        self.assertEqual(new_tuple, ('apple', 'banana', 'orange', 'grape'))
        # Also verify that the original tuples were not changed.
        self.assertEqual(fruits1, ('apple', 'banana'))

    def test_tuple_count(self):
        numbers = (1, 2, 2, 3, 4, 2)
        self.assertEqual(numbers.count(2), 3)

    def test_tuple_index(self):
        fruits = ('apple', 'banana', 'orange')
        self.assertEqual(fruits.index('banana'), 1)

    def test_tuple_len(self):
        fruits = ('apple', 'banana', 'orange')
        self.assertEqual(len(fruits), 3)

    def test_tuple_unpack(self):
        mixed_tuple = ('Luke', 19, True)
        (name, age, is_skywalker) = mixed_tuple
        self.assertEqual(name, 'Luke')
        self.assertEqual(age, 19)
        self.assertTrue(is_skywalker)

    def test_tuple_slice(self):
        fruits = ('apple', 'banana', 'orange')
        new_slice = fruits[1:3]
        self.assertEqual(('banana', 'orange'), new_slice)

if __name__ == '__main__':
    unittest.main()
