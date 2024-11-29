import scrapy

class UnsplashScraperItem(scrapy.Item):
    image_url = scrapy.Field()   # URL изображения
    title = scrapy.Field()       # Название изображения
    category = scrapy.Field()    # Категория изображения
    images = scrapy.Field()      # Поле для Scrapy ImagesPipeline
    image_paths = scrapy.Field() # Локальный путь к файлу
