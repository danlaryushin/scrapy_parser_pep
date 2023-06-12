import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org"]

    def parse(self, response):
        index = response.css('section[id="numerical-index"]')
        pep_links = index.css('a[href^="pep-"]')
        for pep_link in pep_links[20:]:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        info = response.css('h1.page-title::text').get().split(' – ')
        data = {
            'number': info[0].split()[-1],
            'name': info[-1],
            'status': response.css('abbr::text').get()
        }
        yield PepParseItem(data)
