import scrapy

from pep_parse.items import PepParseItem
from ..settings import ALLOWED_DOMAIN


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ALLOWED_DOMAIN
    start_urls = [f'https://{allowed_domains}/']

    def parse(self, response):
        index = response.css('section[id="numerical-index"]')
        pep_links = index.css('a[href^="pep-"]')
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        info = response.css('h1.page-title::text').get().split(' – ')
        number = info[0].split()[-1]
        name = info[-1]
        status = response.css('abbr::text').get()
        data = {
            'number': number,
            'name': name,
            'status': status
        }
        yield PepParseItem(data)
