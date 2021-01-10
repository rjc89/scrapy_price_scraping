import scrapy
from price_scraping.items import ProductItem
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join
from scrapy.utils.markup import remove_tags

class Ecommerce(scrapy.Spider):
   name = "ecommerce"
   start_urls = ["https://www.ebuyer.com/store/Computer/cat/Monitors",]

   def parse(self, response):
       item_loader = ItemLoader(item=ProductItem(), response=response)
       item_loader.default_input_processor = MapCompose(remove_tags)

       item_loader.add_css("product", "h1[itemprop='name']")
       item_loader.add_css("price", "span[itemprop=price]")
       item_loader.add_css("stock", "span[itemprop=’stock’]")
       item_loader.add_css("category", "a[data-track='Breadcrumb']")
       print(item_loader.load_item()) 
       return item_loader.load_item()