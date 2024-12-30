import scrapy

class NewSpyder(scrapy.Spider):
  name = "newspyder"
  start_urls = ["https://vibegaming.com.bd/?srsltid=AfmBOorATma_-VxkXP8IQcG7d0q6FvFyCptzMQStSVZoelTUmDKV_WWB"]


  def parse(self, response):
    for products in response.css("div.product-wrapper"):
      try:
        yield{
          'name': products.css("h3.product-name ::text").get(),
          'price': products.css("span.screen-reader-text ::text").get().replace("Original price was: ৳", "").replace(",", ""),
          'link': products.css("h3.product-name a").attrib["href"],
        }
      except:
        yield{
        'name': products.css("h3.product-name ::text").get(),
        'price': "sold",
        'link': products.css("h3.product-name a").attrib["href"],
        }

