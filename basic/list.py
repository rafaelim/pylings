import unittest

class TestList(unittest.TestCase):
    def test_list_len(self):
        self.assertEqual(len(['apple', 'banana', 'orange']), 3)

    def test_list_clear(self):
        fruits = ['apple', 'banana', 'orange']
        self.assertEqual(len(fruits), 3)
        fruits.clear()
        self.assertEqual(len(fruits), 0)

    def test_list_modify_item(self):
        fruits = ['apple', 'banana', 'orange']
        fruits[1] = 'grape'
        self.assertEqual(fruits, ['apple', 'grape', 'orange'])

    def test_list_append(self):
        fruits = ['apple', 'banana', 'orange']
        self.assertEqual(len(fruits), 3)
        fruits.append('melon')
        self.assertEqual(len(fruits), 4)
        self.assertEqual(fruits[-1], 'melon')

    def test_list_extend(self):
        fruits = ['apple', 'banana']
        more_fruits = ['orange', 'grape']
        fruits.extend(more_fruits)
        self.assertEqual(fruits, ['apple', 'banana', 'orange', 'grape'])

    def test_list_concatenation(self):
        fruits = ['apple', 'banana']
        more_fruits = ['orange', 'grape']
        new_list = fruits + more_fruits
        self.assertEqual(new_list, ['apple', 'banana', 'orange', 'grape'])

    def test_list_insert(self):
        fruits = ['apple', 'banana', 'orange']
        self.assertEqual(len(fruits), 3)
        fruits.insert(1, 'melon')
        self.assertEqual(len(fruits), 4)
        self.assertEqual(fruits[1], 'melon')
        self.assertEqual(fruits[-1], 'orange')

    def test_list_remove(self):
        fruits = ['apple', 'banana', 'orange']
        self.assertEqual(len(fruits), 3)
        self.assertEqual(fruits[1], 'banana')
        fruits.remove('banana')
        self.assertEqual(len(fruits), 2)
        self.assertEqual(fruits[1], 'orange')

    def test_list_pop(self):
        fruits = ['apple', 'banana', 'orange']
        self.assertEqual(len(fruits), 3)
        popped_item = fruits.pop()
        self.assertEqual(len(fruits), 2)
        self.assertEqual(popped_item, 'orange')

    def test_list_pop_index(self):
        fruits = ['apple', 'banana', 'orange']
        self.assertEqual(len(fruits), 3)
        popped_item = fruits.pop(1)
        self.assertEqual(len(fruits), 2)
        self.assertEqual(popped_item, 'banana')

    def test_list_sort_inplace(self):
        num_list = [1, 2, 5, 3, 4]
        self.assertIsNone(num_list.sort())
        self.assertEqual(num_list, [1, 2, 3, 4, 5])

    def test_list_sort_inplace_reverse(self):
        num_list = [1, 2, 5, 3, 4]
        num_list.sort(reverse=True)
        self.assertEqual(num_list, [5, 4, 3, 2, 1])

    def test_list_sort(self):
        num_list = [1, 2, 5, 3, 4, 6, 9, 7, 0, 8]
        sorted_num_list = sorted(num_list)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], sorted_num_list)

    def test_list_sort_reverse(self):
        num_list = [1, 2, 5, 3, 4, 6, 9, 7, 0, 8]
        sorted_num_list = sorted(num_list, reverse=True)
        self.assertEqual([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], sorted_num_list)

    def test_list_max(self):
        num_list = [1, 2, 5, 3, 4, 6, 9, 7, 0, 8]
        self.assertEqual(max(num_list), 9)

    def test_list_min(self):
        num_list = [1, 2, 5, 3, 4, 6, 9, 7, 0, 8]
        self.assertEqual(min(num_list), 0)

    def test_list_map_doubled(self):
        num_list = [2, 4, 6, 8]
        doubled = map(lambda num: num * 2, num_list)
        self.assertEqual([4, 8, 12, 16], list(doubled))

    def test_list_list_comp_doubled(self):
        num_list = [2, 4, 6, 8]
        doubled = [num * 2 for num in num_list]
        self.assertEqual([4, 8, 12, 16], list(doubled))
        
    def test_list_filter_even(self):
        num_list = [1, 2, 3, 4, 5]
        only_even = filter(lambda num: num % 2 == 0, num_list)
        self.assertEqual([2, 4], list(only_even))

    def test_list_list_comp_even(self):
        num_list = [1, 2, 3, 4, 5]
        only_even = [num for num in num_list if num % 2 == 0]
        self.assertEqual([2, 4], list(only_even))

    def test_list_enumarate(self):
        num_list = [1, 2, 3, 4, 5]
        self.assertEqual(list(enumerate(num_list)), [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)])

    def test_list_slicing(self):
        numbers = [0, 1, 2, 3, 4, 5]
        self.assertEqual(numbers[2:5], [2, 3, 4])
        self.assertEqual(numbers[:3], [0, 1, 2])
        self.assertEqual(numbers[3:], [3, 4, 5])
        self.assertEqual(numbers[::-1], [5, 4, 3, 2, 1, 0])

    def test_list_value_exists(self):
        fruits = ['apple', 'banana', 'orange']
        self.assertIn('banana', fruits)
        self.assertNotIn('kiwi', fruits)

if __name__ == '__main__':
    unittest.main()
