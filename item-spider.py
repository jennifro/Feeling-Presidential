import scrapy


class scrapeItem(scrapy.Item):
    """Define relevant data to store from json crawl."""

    title = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()

##########################################################
# in SPIDER 

import scrapy
from speechscrape.items import scrapeItem ## CHANGE THIS LINE W/ LOCATION OF ITEMS.


class Spider(scrapy.Spider):
    """Spider to scrape website for data"""

    name = "prezspeech"
    allowed_domains = ["millercenter.org"]

    # grabbing the Crisis of Confidence speech, Jimmy Carter
    start_urls = ["http://millercenter.org/president/kennedy/speeches/speech-3365",   # inaugural
                  "http://millercenter.org/president/kennedy/speeches/speech-5742"]   # first state of union

    def parse(self, response):
        for sel in response.xpath('/article'):
            item = scrapeItem()
            title = sel.xpath("//div/h1[@id='amprestitle']/text()").extract()
            author = sel.xpath("//div[@id='innercontent']/h2/text()").extract()
            text = sel.xpath("//div[@id='transcript']/p/text()").extract()
            print title, author, text