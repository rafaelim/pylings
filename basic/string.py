import unittest

class TestString(unittest.TestCase):
    def test_strings(self):
        my_string = 'Hello, world!'
        multi_line_string = """
            This is a string
            that spans multiple lines.
        """
        self.assertIsNotNone(my_string)
        self.assertIsNotNone(multi_line_string)

    def test_string_slice(self):
        my_string = "Python"
        self.assertEqual(my_string[0], 'P')
        self.assertEqual(my_string[1:], 'ython')

    def test_string_upper(self):
        my_string = "Python"
        self.assertEqual(my_string.upper(), 'PYTHON')

    def test_string_lower(self):
        my_string = "Python"
        self.assertEqual(my_string.lower(), 'python')

    def test_string_strip(self):
        my_string = "   Python   "
        self.assertEqual(my_string.strip(), 'Python')

    def test_string_split(self):
        movie_title = "Star Wars: Episode IV - A New Hope"
        self.assertEqual(list(movie_title.split(' ', 3)), ['Star', 'Wars:', 'Episode', 'IV - A New Hope'])

    def test_string_join(self):
        movie_title = ['Star Wars', 'Episode IV', 'A New Hope']
        self.assertEqual(' - '.join(movie_title), 'Star Wars - Episode IV - A New Hope')

    def test_string_replace(self):
        movie_title = "star-wars-episode-iv-a-new-hope"
        self.assertEqual(movie_title.replace('-', ' '), 'star wars episode iv a new hope')

    def test_string_find(self):
        movie_title = "Star Wars: Episode IV - A New Hope"
        self.assertEqual(movie_title.find(':'), 9)
        
    def test_string_index(self):
        movie_title = "Star Wars: Episode IV - A New Hope"
        self.assertEqual(movie_title.index(':'), 9)

    def test_string_find_invalid(self):
        movie_title = "Star Wars: Episode IV - A New Hope"
        self.assertEqual(movie_title.find('/'), -1)
        
    def test_string_index_invalid(self):
        movie_title = "Star Wars: Episode IV - A New Hope"
        with self.assertRaises(ValueError):
            movie_title.index('/')

    def test_string_startswith(self):
        movie_title = "Star Wars: Episode IV - A New Hope"
        self.assertTrue(movie_title.startswith('Star'))
        self.assertFalse(movie_title.startswith('star'))

    def test_string_endswith(self):
        movie_title = "Star Wars: Episode IV - A New Hope"
        self.assertTrue(movie_title.endswith('Hope'))
        self.assertFalse(movie_title.endswith('hope'))

    def test_string_count(self):
        sentence = "one two one three one four"
        self.assertEqual(sentence.count('one'), 3)

    def test_string_immutability(self):
        my_string = "Python"
        with self.assertRaises(TypeError):
            my_string[0] = 'J'

    def test_string_reverse_slice(self):
        my_string = "Python"
        self.assertEqual(my_string[::-1], "nohtyP")

if __name__ == '__main__':
    unittest.main()
