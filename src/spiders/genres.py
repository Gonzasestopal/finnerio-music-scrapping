# -*- coding: utf-8 -*-
import json
from typing import Iterator, Union

import scrapy
from scrapy import Item, Request, Spider, signals
from scrapy.crawler import Crawler
from scrapy.http import Response
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider

from src.items import Genre
from src.settings import NAPSTER_API_KEY, NAPSTER_API_URL
from src.utils import build_url


class Genres(CrawlSpider):
    name = "genres"

    custom_settings = {}

    @classmethod
    def from_crawler(cls, crawler: Crawler, *args, **kwargs):
        spider = super().from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def __init__(self, *args, **kwargs):
        Spider.__init__(self, *args, **kwargs)

    def start_requests(self) -> Iterator[Request]:
        urls = [
            build_url(NAPSTER_API_URL, self.name, {'apikey': NAPSTER_API_KEY}),
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: Response) -> Iterator[Union[Item, Request]]:
        self.logger.info('request status %s', response.status)
        json_res = json.loads(response.body)
        if not isinstance(json_res, dict) or len(json_res) < 1:
            self.logger.info('empty or malformed response %s', json_res)
            return None

        data = json_res['genres']

        for genre in data:
            loader = ItemLoader(item=Genre())
            loader.add_value('name', genre['name'])
            loader.add_value('href', genre['href'])
            yield loader.load_item()

    def spider_closed(self) -> None:
        pass
