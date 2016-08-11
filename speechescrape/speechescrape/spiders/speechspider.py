import scrapy
# from speechescrape.items import SpeechescrapeItem   # if I need to store in dict


class SpeechSpider(scrapy.Spider):
    """To scrape website for speeches."""

    name = "speeches"
    allowed_domains = ["millercenter.org"]

    start_urls = ["http://millercenter.org/president/kennedy/speeches/speech-3365",   # inaugural
                  "http://millercenter.org/president/kennedy/speeches/speech-5742"]   # first state of union

    def parse(self, response):
        """Parse HTML response."""
            # item = SpeechescrapeItem()       # probably not going to store it in a dict just yet

        yield {
            'title': response.xpath("//div/h1[@id='amprestitle']/text()").extract(),
            'author': response.xpath("//div[@id='innercontent']/h2/text()").extract(),
            'text': response.xpath("//div[@id='transcript']/p/text()").extract()
            }
