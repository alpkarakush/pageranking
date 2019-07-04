import scrapy
import logging
import re


logging.basicConfig(level=logging.DEBUG)

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = [
        'https://en.wikipedia.org/wiki/King%27s_Cross_Thameslink_railway_station',
    ]

    def parse(self, response):
        page_dict = {}

        page_dict['link'] = response.url
        page_dict['outlinks'] = []
        for elem in response.xpath("//div[@id='bodyContent']//a"):
            if re.match(r'^/wiki', str(elem.xpath('@href').get())) and not re.match(r'^/wiki/File', str(elem.xpath('@href').get())):
                page_dict['outlinks'].append("https://en.wikipedia.org" + elem.xpath('@href').get())

        # page_dict['outlinks'] = [ "https://en.wikipedia.org" + outlink.xpath('@href').get() for outlink in response.xpath("//div[@id='bodyContent']//a") if re.match(r'^/wiki', str(outlink.xpath('@href').get())) ]
        page_dict['text'] = response.xpath("//div[@id='bodyContent']//text()[re:test(., '\w+')]").extract()
        
        yield page_dict

        for elem in response.xpath("//div[@id='bodyContent']//a"):
            if re.match(r'^/wiki', str(elem.xpath('@href').get())) and not re.match(r'^/wiki/File', str(elem.xpath('@href').get())):
                next_page = "https://en.wikipedia.org" + elem.xpath('@href').get()
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
