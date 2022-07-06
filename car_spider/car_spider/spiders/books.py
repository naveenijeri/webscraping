from gc import callbacks
# from urllib.request import Request
import scrapy
from scrapy.http import Request


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        books = response.xpath('//h3/a/@href').extract()
        for book in books:
            absolute_url = response.urljoin(book)
            print("absolute urls", absolute_url)
            yield Request(absolute_url, callback=self.parse_book)
        
        #process the next page url
        next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request()
    
    def parse_book(self, response):
        pass
