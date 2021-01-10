import scrapy
class price_spider(scrapy.Spider):
   name = "price_"
   start_urls = ["https://www.ebuyer.com/store/Computer/cat/Monitors", ]

   def parse(self, response):
       item_loader = ItemLoader(item=ProductItem(), response=response)
       item_loader.default_input_processor = MapCompose(remove_tags)

       item_loader.add_css("product", "a[data-track='title']")
    #    item_loader.add_css("price", "span[itemprop=price]")
    #    item_loader.add_css("stock", "span[itemprop=’stock’]")
    #    item_loader.add_css("category", "a[data-track='Breadcrumb']")
       print('this is the output', item_loader.load_item) 
       return item_loader.load_item()