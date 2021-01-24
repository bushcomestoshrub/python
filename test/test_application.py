from app_context import src as app

import unittest


class ApplicationTest(unittest.TestCase):

    def test_hello(self):
        expected = "Hi There"
        self.assertEqual(expected, app.test.hello())

    def test_good_bye(self):
        expected = "Adios"
        self.assertEqual(expected, app.test.good_bye())

    def test_person(self):
        expected = "John"
        p = app.test.Person(expected)
        self.assertEqual(expected, p.name)


if __name__ == '__main__':
    unittest.main()
