# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NcalhdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Director(scrapy.Item):
    id = scrapy.Field()
    first_name = scrapy.Field()
    last_name = scrapy.Field()
    email = scrapy.Field()
    phone_number = scrapy.Field()
    fax_number = scrapy.Field()
    county = scrapy.Field()
    role = scrapy.Field()
