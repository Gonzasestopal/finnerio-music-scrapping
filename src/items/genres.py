from scrapy import Item, Field
from scrapy.loader.processors import TakeFirst


class GenreItem(Item):
    name = Field(output_processor=TakeFirst())
    href = Field(output_processor=TakeFirst())
