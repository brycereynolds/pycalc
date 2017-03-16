from calculator import Calculator
import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

    def test_dumb(self):
        self.assertEqual(self.calc.submit('5'), 5)

    def test_stub1(self):
        self.assertEqual(self.calc.submit('5 + 5'), 10)

    def test_stub2(self):
        self.assertEqual(self.calc.submit('15 + 5 - 10'), 10)

    def test_stub3(self):
        self.assertEqual(self.calc.submit('5 * 5'), 25)

    def test_stub4(self):
        self.assertEqual(self.calc.submit('(2 + 3) * 5'), 25)

if __name__ == '__main__':
    unittest.main()