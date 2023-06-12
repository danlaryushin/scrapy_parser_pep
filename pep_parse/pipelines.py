import csv
from datetime import datetime as dt

from scrapy.exceptions import DropItem

from .settings import BASE_DIR, DT_FORMAT, RESULTS_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.counter = {}

    def process_item(self, item, spider):
        try:
            status = item['status']
            self.counter[status] = self.counter.get(status, 0) + 1
        except DropItem:
            raise DropItem('Drop item {item} from item_pipeline')
        return item

    def close_spider(self, spider):
        time = dt.now().strftime(DT_FORMAT)
        FILE_NAME = f'status_summary_{time}.csv'
        path = BASE_DIR / RESULTS_DIR / FILE_NAME
        with open(path, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file, dialect='unix',
                                escapechar=',', quoting=csv.QUOTE_NONE)
            file.write('Статус,Количество\n')
            writer.writerows(
                (
                    *self.counter.items(),
                    ('Total', sum(self.counter.values()))
                )
            )
