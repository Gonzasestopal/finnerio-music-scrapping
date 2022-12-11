import unittest

from scrapy.http import Response

from src.spiders import GenreSpider


class GenresSpiderTest(unittest.TestCase):

    def setUp(self):
        self.spider = GenreSpider()

    def _test_item_results(self, results, expected_length):
        count = 0
        for item in results:
            self.assertIsNotNone(item['name'])
            self.assertIsNotNone(item['href'])
            count += 1
        self.assertEqual(count, expected_length)

    def test_parse(self):
        with open('src/tests/fixtures/genres.json', 'rb') as genres_data:
            response = Response(body=genres_data.read(), status=200, url='ok')
            parsed_data = self.spider.parse(response)
            self._test_item_results(parsed_data, 23)
