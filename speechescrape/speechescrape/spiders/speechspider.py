import scrapy
# from speechescrape.items import SpeechescrapeItem   # if I need to store in dict


class SpeechSpider(scrapy.Spider):
    """To scrape website for speeches."""

    name = "speeches"
    allowed_domains = ["millercenter.org"]

    start_urls = ["http://millercenter.org/president/kennedy/speeches/speech-3365",   # inaugural
                  "http://millercenter.org/president/kennedy/speeches/speech-5742"]   # first state of union

    def parse(self, response):
        for sel in response.xpath('//article'):
            # item = SpeechescrapeItem()       # probably not going to store it in a dict just yet
            title = sel.xpath("//div/h1[@id='amprestitle']/text()").extract()
            author = sel.xpath("//div[@id='innercontent']/h2/text()").extract()
            text = sel.xpath("//div[@id='transcript']/p/text()").extract()
            yield title, author, text
