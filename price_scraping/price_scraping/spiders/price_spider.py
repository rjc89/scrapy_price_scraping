import scrapy
from price_scraping.items import *
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join
from scrapy.utils.markup import remove_tags

class Ecommerce(scrapy.Spider):
   name = "ecommerce"
   allowed_domains = ['www.ebuyer.com']
   start_urls = ["https://www.ebuyer.com/store/Computer/cat/Monitors"]

   def parse(self, response):
      l = ItemLoader(item=ProductItem(), response=response)
      item_loader.default_input_processor = MapCompose(remove_tags)

      l.add_xpath("product", '//p[@class="drop-product-title"]')
      #  #item_loader.add_css("price", "data-product-price")
      #  l.add_xpath('site_title', '//title/text()')
      l.add_xpath('link', '//a/@href')

      return l.load_item()