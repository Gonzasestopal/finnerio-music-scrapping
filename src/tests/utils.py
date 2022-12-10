import unittest

from utils.urls import build_url


class RequestTestCase(unittest.TestCase):

    def test_build_url(self):
        expected_url = 'https://api.napster.com/genres?apikey=abc'

        new_url = build_url('https://api.napster.com/', 'genres', {'apikey': 'abc'})

        self.assertEqual(new_url, expected_url, 'should include path, args and base url')

if __name__ == '__main__':
    unittest.main()
