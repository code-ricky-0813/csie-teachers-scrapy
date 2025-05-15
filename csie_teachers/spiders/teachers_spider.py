import scrapy
from csie_teachers.items import CsieTeachersItem

class TeachersSpider(scrapy.Spider):
    name = "teachers"
    start_urls = ["https://csie.asia.edu.tw/zh_tw/associate_professors_2"]

    def parse(self, response):
        profiles = response.css('.i-member-profile-data-wrap')
        for profile in profiles:
            name = profile.css('.member-data-value-name::text').get()
            expertise = profile.css('.member-data-value-7::text').get()
            if not expertise:
                expertise = "無"
            item = CsieTeachersItem(name=name, expertise=expertise)
            yield item
