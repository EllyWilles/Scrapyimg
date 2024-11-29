import csv
from scrapy.exceptions import DropItem

class CsvWriterPipeline:

    def open_spider(self, spider):
        self.file = open('images_data.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(self.file, fieldnames=['image_url', 'image_path', 'title', 'category'])
        self.writer.writeheader()

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if not item.get('image_url'):
            raise DropItem("Missing image URL in %s" % item)
        
        image_path = item.get('images', [{}])[0].get('path', '')
        self.writer.writerow({
            'image_url': item['image_url'],
            'image_path': image_path,
            'title': item['title'],
            'category': item['category']
        })
        return item
