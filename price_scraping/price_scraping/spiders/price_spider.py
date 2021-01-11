import scrapy
from price_scraping.items import *
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join
from scrapy.utils.markup import remove_tags

class Ecommerce(scrapy.Spider):
   name = "ecommerce"
   #allowed_domains = ['www.ebuyer.com']
   start_urls = ["https://www.ebuyer.com/store/Computer/cat/Monitors"]

   def parse(self, response):
      for Prod in response.xpath("//p[@class='drop-product-title']"):
         print('************', Prod)
         l = ItemLoader(item=ProductItem(), response=response)
         #l.default_input_processor = MapCompose(remove_tags)

         l.add_xpath("product", "//p[@class='drop-product-title']")
      # l.add_css("price", "data-product-price")

      #   //div[contains(@class,"item-div")]
      # l.add_xpath('site_title', '//title/text()')
         l.add_xpath('link', '//a/@href')
         # l.add_xpath('product', '')
         return l.load_item()