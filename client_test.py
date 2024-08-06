import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        expected = [
            ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2),
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
        ]

        for quote, exp in zip(quotes, expected):
            self.assertEqual(getDataPoint(quote), exp)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        expected = [
            ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2),
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
        ]

        for quote, exp in zip(quotes, expected):
            self.assertEqual(getDataPoint(quote), exp)

    def test_getDataPoint_noBidPrice(self):
        quote = {'top_ask': {'price': 100.0, 'size': 50}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': '0.0', 'size': 50}, 'id': '0.109974697771', 'stock': 'XYZ'}
        self.assertEqual(getDataPoint(quote), ('XYZ', 0.0, 100.0, (0.0 + 100.0) / 2))

    def test_getDataPoint_noAskPrice(self):
        quote = {'top_ask': {'price': '0.0', 'size': 50}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.0, 'size': 50}, 'id': '0.109974697771', 'stock': 'XYZ'}
        self.assertEqual(getDataPoint(quote), ('XYZ', 120.0, 0.0, (120.0 + 0.0) / 2))

    def test_getDataPoint_invalidPrice(self):
        quote = {'top_ask': {'price': 'invalid', 'size': 50}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 'invalid', 'size': 50}, 'id': '0.109974697771', 'stock': 'XYZ'}
        with self.assertRaises(ValueError):
            getDataPoint(quote)

if __name__ == '__main__':
    unittest.main()
