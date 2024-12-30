import scrapy

class StaryScraper(scrapy.Spider):
    name = "staryscraper"
    start_urls = ["https://www.startech.com.bd/accessories/keyboards"]

    def parse(self, response):
        for product in response.css("div.p-item-details"):
            try:
                name = product.css("h4.p-item-name a::text").get()
                print(name)

                price = product.css("span.p-item-price::text").get()
                if price:
                    price = price.replace("৳", "").replace(",", "")
                else:
                    price = product.css("div.p-item-price span::text").get()
                    if price:
                        price = price.replace("৳", "").replace(",", "")
                    else:
                        price = "Out of stock"

                link = product.css("h4.p-item-name a::attr(href)").get()  # Fix for link extraction
                print(link)

                yield {
                    'name': name,
                    'price': price,
                    'link': link,
                }
            except Exception as e:
                yield {
                    "name": "Unable to scrap",
                    "price": "Unable to scrap",
                    "link": "Unable to scrap",
                }
        next_page = response.css('ul.pagination li a:contains("NEXT")').attrib['href']
        if next_page is not None:
          yield response.follow(next_page, callback=self.parse)