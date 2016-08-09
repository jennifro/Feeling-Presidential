import scrapy


class SpeechescrapeItem(scrapy.Item):
    """Relevant data from scrapy crawl."""

    title = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()
