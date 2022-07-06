from http.client import responses
from urllib import response
import scrapy
from scrapy_splash import SplashRequest

class BairelSpider(scrapy.Spider):
    name = 'bairel'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse,endpoint='render.html')
   
    def parse(self,response):
        script = """function main(splash)
            assert(splash:go(splash.args.url))
            splash:wait(0.3)
            button = splash:select("a")
            splash:set_viewport_full()
            splash:wait(0.1)
            button:mouse_click()
            splash:wait(1)
            return {url = splash:url(),
                    html = splash:html()}
        end"""
        yield SplashRequest(url=response.url, callback=self.start_extract, endpoint='render.html', args={'lua_source':script})

    def start_extract(self, response):
        print("RESULT",response.text)
      