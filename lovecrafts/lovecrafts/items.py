# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def decimals(value):
    return value.strip(' ')

class LovecraftsItem(scrapy.Item):

    brand = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    product_type = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    name = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    details = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    shades = scrapy.Field(input_processor = MapCompose(remove_tags, decimals), output_processor = TakeFirst())

    pass
