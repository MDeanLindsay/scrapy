import scrapy


class WebsSpider(scrapy.Spider):
    name = 'webs'
    allowed_domains = ['https://www.yarn.com/']
    urls = ['https://www.yarn.com/categories/knitting-yarn?page='.format(i) for i in range (1,200)]
    start_urls = urls

    def parse(self, response):
        items = response.css('div.product-summary')
        for item in items:
            try:
                yield {
                    'brand' : item.css('p.product-summary__brand::text').get(),
                    'name' : item.css('p.product-summary__name a::text').get(),
                    'price' : item.css('p.product-prices__price span::text').get(),
                    'size' : item.css('p.product-prices__price span:nth-child(2)::text').get(),
                    'weight' : item.css('ul.list-reset li:nth-child(1)::text').get(),
                    'guage' : item.css('ul.list-reset li:nth-child(2)::text').get(),
                    'fiber' : item.css('ul.list-reset li:nth-child(3)::text').get(),
                    'grams_yards' : items.css('ul.list-reset li:nth-child(4)::text').get()
                }
            except:
                pass
