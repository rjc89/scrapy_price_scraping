# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PriceScrapingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product = Field()
    price = Field()
    category = Field()
    stock = Field()
    pass
