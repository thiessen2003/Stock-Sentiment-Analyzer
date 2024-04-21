import unittest
from SentimentAnalyzer import SentimentAnalyzer


import unittest
from WebScrapper import WebScrapper

class TestSentimentAnalyzer(unittest.TestCase):

    def setUp(self):
        self.stock_tester = WebScrapper()
        self.wrong_df = "../data/nullcsv.csv"
        self.right_df = "../data/stocklist.csv"

    def test_read_stocks_null(self):
        self.assertEqual(self.stock_tester.read_stocks(self.wrong_df), "An error has occured")

    def test_read_stocks_not_null(self):
        self.assertIsNotNone(self.stock_tester.read_stocks(self.wrong_df))

    def test_stock_exists_false(self):
        self.assertFalse(self.stock_tester.stock_exists("MSTFS", self.right_df))

    def test_stock_exists_true(self):
        self.assertTrue(self.stock_tester.stock_exists("META", self.right_df))