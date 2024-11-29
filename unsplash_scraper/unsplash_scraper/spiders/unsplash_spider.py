import scrapy
from unsplash_scraper.items import UnsplashScraperItem

class UnsplashSpider(scrapy.Spider):
    name = "unsplash_spider"
    allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com/"]

    def parse(self, response):
        # Найти ссылки на категории
        categories = response.css('a[href^="/t/"]::attr(href)').getall()
        self.logger.info(f"Найдено категорий: {len(categories)}")

        for category in categories:
            yield response.follow(category, callback=self.parse_category)

    def parse_category(self, response):
        # Обработка страниц категорий
        self.logger.info(f"Обрабатываем категорию: {response.url}")

        # Извлекаем изображения из категории
        images = response.css('img[srcset]')
        
        # Проверяем, что мы извлекаем изображения
        self.logger.info(f"Найдено изображений: {len(images)}")

        for image in images:
            item = UnsplashScraperItem()
            
            # Извлекаем URL изображения (для этого используем srcset)
            image_url = image.css('::attr(srcset)').get()
            item['image_url'] = image_url

            # Извлекаем название изображения (alt-тег)
            title = image.css('::attr(alt)').get()
            item['title'] = title

            # Извлекаем категорию из URL
            item['category'] = response.url.split("/")[-1]  # категория из URL

            # Печатаем каждый элемент, чтобы проверить, что они корректно генерируются
            self.logger.info(f"Генерируем элемент: {item}")

            # Возвращаем элемент
            yield item
