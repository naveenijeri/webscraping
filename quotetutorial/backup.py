import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        items = QuotetutorialItem()
        # title = response.css('title::text').extract_first()
        # description = response.css('span.text::text').extract_first()
        # descriptions = response.xpath("//span[@class='text']/text()").extract()
        # yield {'titletext': title, 'descriptions': descriptions}

        all_div_quotes = response.css('div.quote')
        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            # yield {
            #     'title': title,
            #     'author': author,
            #     'tag': tag
            # }
            items["title"] = title
            items["author"] = author
            items["tag"] = tag
            yield items
