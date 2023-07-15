import scrapy
from ..items import QuotesscrapeItem

"""
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        items = QuotesscrapeItem()

        for quote in response.css("div.quote"):
            title = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("a.tag::text").getall()

            items["title"] = title  # L.H.S `title` is from items.py
            # and R.H.S `title` is variable from quotes_spider.py file.
            items["author"] = author
            items["tags"] = tags

            # yield {"title": title, "author": author, "tags": tags}

            yield items

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
"""


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = ["https://quotes.toscrape.com/page/1/"]
    page_number = 2

    def parse(self, response):
        items = QuotesscrapeItem()

        for quote in response.css("div.quote"):
            title = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("a.tag::text").getall()

            items["title"] = title  # L.H.S `title` is from items.py
            # and R.H.S `title` is variable from quotes_spider.py file.
            items["author"] = author
            items["tags"] = tags

            # yield {"title": title, "author": author, "tags": tags}

            yield items
        next_page = f"https://quotes.toscrape.com/page/{QuotesSpider.page_number}/"

        if QuotesSpider.page_number < 11:
            QuotesSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
