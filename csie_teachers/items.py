import scrapy

class CsieTeachersItem(scrapy.Item):
    name = scrapy.Field()
    expertise = scrapy.Field()
