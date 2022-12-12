# -*- coding: utf-8 -*-
import json
from typing import Iterator, Union

import requests
import scrapy
from scrapy import Item, Request, Spider, signals
from scrapy.crawler import Crawler
from scrapy.http import Response
from scrapy.spiders import CrawlSpider

from src.db import Database
from src.settings import NAPSTER_API_KEY, NAPSTER_API_URL
from src.utils import build_url, parse_querystring


class SongSpider(CrawlSpider):
    name = "songs"

    custom_settings = {}

    @classmethod
    def from_crawler(cls, crawler: Crawler, *args, **kwargs):
        spider = super().from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def __init__(self, *args, **kwargs):
        self.database = Database()
        Spider.__init__(self, *args, **kwargs)

    def start_requests(self) -> Iterator[Request]:
        response = requests.get(
            build_url(NAPSTER_API_URL, 'genres', {'apikey': NAPSTER_API_KEY})
        )

        urls = []

        for genre in response.json()['genres']:
            path = '/'.join(['genres', genre['id'], 'tracks', 'top'])
            urls.append(
                build_url(NAPSTER_API_URL, path, {'apikey': NAPSTER_API_KEY, 'range': "week", 'name': genre['name']})
            )

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response: Response) -> Iterator[Union[Item, Request]]:
        self.logger.info('request status %s', response.status)
        parse_result = parse_querystring(response.url)
        json_res = json.loads(response.body)
        if not isinstance(json_res, dict) or len(json_res) < 1:
            self.logger.info('empty or malformed response %s', json_res)
            return None

        data = json_res['tracks']

        for track in data:
            genre_id, _ = self.database.fetch_genre_by_name(parse_result['name'][0])
            artist_id, _ = self.database.fetch_artist_by_name(track['artistName'])
            album_id, _ = self.database.fetch_album_by_name(track['albumName'])
            self.database.insert_song(track['name'], artist_id, album_id, genre_id)

    def spider_closed(self) -> None:
        self.database.cur.close()
        self.database.conn.close()
