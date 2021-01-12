import scrapy
from price_scraping.items import *
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join
from scrapy.utils.markup import remove_tags
from scrapy.selector import Selector

class Ecommerce(scrapy.Spider):
   name = "ecommerce"
   #allowed_domains = ['www.ebuyer.com']
   start_urls = ["https://www.ebuyer.com/store/Components/cat/Processors-AMD"]

   def parse(self, response):
      products = Selector(response).xpath('//div[@class="drop-product-title"]')
      for Prod in products: #response.xpath('p[@class="drop-product-title"]'):   

         l = ItemLoader(item=ProductItem(), response=response)
         l.default_input_processor = MapCompose(remove_tags)

         l.add_xpath("product", '//div[@class="drop-product-title"]')

         return l.load_item()