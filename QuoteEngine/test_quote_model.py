import unittest
from QuoteModel import QuoteModel


class TestQuoteModel(unittest.TestCase):
    def test_validquote(self):
        a = QuoteModel('Can you hear me Watson ', ' Alexander Bell')
        self.assertEqual(str(a), '"Can you hear me Watson" - Alexander Bell')

    def test_quote_is_not_a_string(self):
        with self.assertRaises(ValueError):
            _ = QuoteModel('', 'John')

    def test_author_is_not_a_string(self):
        with self.assertRaises(ValueError):
            _ = QuoteModel('My quote', '')

    def test_from_line(self):
        a = QuoteModel.from_line('"To be or not to be" - Shakespaere')
        self.assertEqual(str(a), '"To be or not to be" - Shakespaere')

    def test_from_line_nodash(self):
        with self.assertRaises(ValueError):
            _ = QuoteModel.from_line('"To be or not to be" Shakespaere')

    def test_from_line_not_a_string(self):
        with self.assertRaises(ValueError):
            _ = QuoteModel.from_line(5)


if __name__ == '__main__':
    unittest.main()
