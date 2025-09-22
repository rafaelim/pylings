import unittest

class TestDict(unittest.TestCase):
    def test_dict(self):
        car = {
            'brand': 'Volkswagen',
            'model': 'Nivus',
            'year': 2025
        }
        self.assertEqual(car['brand'], 'Volkswagen')
        self.assertEqual(car.get('brand'), 'Volkswagen')

    def test_dict_setdefault(self):
        car = {
            'brand': 'Volkswagen',
            'model': 'Nivus',
            'year': 2025
        }
        self.assertEqual(car.get('color'), None)
        with self.assertRaises(KeyError):
            car['color']
        self.assertEqual(car.setdefault('Color', 'Grey'), 'Grey')
        self.assertEqual(car['Color'], 'Grey')

    def test_dict_del_key(self):
        car = {
            'brand': 'Volkswagen',
            'model': 'Nivus',
            'year': 2025
        }
        self.assertEqual(car['year'], 2025)
        del car['year']
        with self.assertRaises(KeyError):
            car['year']

    def test_dict_pop_key(self):
        car = {
            'brand': 'Volkswagen',
            'model': 'Nivus',
            'year': 2025
        }
        self.assertEqual(car['year'], 2025)
        popped_key = car.pop('year')
        self.assertEqual(popped_key, 2025)
        with self.assertRaises(KeyError):
            car['year']

    def test_dict_pop_with_default(self):
        car = {
            'brand': 'Volkswagen',
            'model': 'Nivus',
            'year': 2025
        }
        popped_value = car.pop('color', 'unknown')
        self.assertEqual(popped_value, 'unknown')

    def test_dict_keys(self):
        car = {
            'brand': 'Volkswagen',
            'model': 'Nivus',
            'year': 2025
        }
        self.assertEqual(list(car.keys()), ['brand', 'model', 'year'])

    def test_dict_values(self):
        car = {
            'brand': 'Volkswagen',
            'model': 'Nivus',
            'year': 2025
        }
        self.assertEqual(list(car.values()), ['Volkswagen', 'Nivus', 2025])

    def test_dict_items(self):
        car = {
            'brand': 'Volkswagen',
            'model': 'Nivus',
            'year': 2025
        }
        self.assertEqual(list(car.items()), [('brand', 'Volkswagen'), ('model', 'Nivus'), ('year', 2025)])

    def test_dict_clear(self):
        car = {
            'brand': 'volkswagen',
            'model': 'nivus',
            'year': 2025
        }
        self.assertEqual(len(list(car.keys())), 3)
        car.clear()
        self.assertEqual(len(list(car.keys())), 0)

    def test_dict_update(self):
        car = {
            'brand': 'Volkswagen',
            'model': 'Nivus'
        }
        self.assertEqual(car, {
            'brand': 'Volkswagen',
            'model': 'Nivus'
        })
        updates = {
            'year': 2025,
            'color': 'black'
        }
        car.update(updates)
        self.assertEqual(car, {
            'brand': 'Volkswagen',
            'model': 'Nivus',
            'year': 2025,
            'color': 'black'
        })

    def test_dict_key_exists(self):
        car = {
            'brand': 'volkswagen',
            'model': 'nivus',
            'year': 2025
        }
        self.assertIn('brand', car)
        self.assertNotIn('color', car)

if __name__ == '__main__':
    unittest.main()
