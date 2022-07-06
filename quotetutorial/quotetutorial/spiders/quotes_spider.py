from gc import callbacks
import scrapy
from ..items import QuotetutorialItem
from scrapy.http import FormRequest

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        print("token:", token)
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'naveen.ijeri123@gmail.com',
            'password': 'naveen072!'
        }, callback=self.start_scraping)
    
    def start_scraping(self, response):
        print("start scraping function")
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