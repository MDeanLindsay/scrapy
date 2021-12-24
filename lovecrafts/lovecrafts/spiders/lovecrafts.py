import scrapy
from lovecrafts.items import LovecraftsItem
from scrapy.loader import ItemLoader

class LovecraftsSpider(scrapy.Spider):
    name = 'lovecrafts'
    allowed_domains = ['lovecrafts.com']
    start_urls = ['https://lovecrafts.com/en-us/l/yarns']

    def parse(self, response):

        for item in response.css('div.card'):

                l = ItemLoader(item = LovecraftsItem(), selector = item)

                l.add_css('brand', 'a::attr(data-brand)')
                l.add_css('product_type', 'a::attr(data-producttype)')
                l.add_css('name', 'a::attr(data-name)')
                l.add_css('details', 'a::attr(data-subtitle)')
                l.add_css('price', 'a::attr(data-price)')
                l.add_css('shades', 'figure.card-view span.card-img-wrapper span.count')
                
                yield l.load_item()
                
        next_page = response.css('a.pagination-button.next-page::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
