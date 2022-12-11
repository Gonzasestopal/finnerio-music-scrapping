from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from src.spiders import GenreSpider

process = CrawlerProcess(get_project_settings())
process.crawl(GenreSpider)
process.start()
