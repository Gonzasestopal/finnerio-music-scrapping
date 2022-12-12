from scrapy import Item, Field
from itemloaders.processors import TakeFirst


class GenreItem(Item):
    name = Field(output_processor=TakeFirst())
