# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from ncalhd.items import Director


class DirectorsSpider(CrawlSpider):
    name = 'directors'
    allowed_domains = ['www.ncalhd.org']
    start_urls = ['http://www.ncalhd.org/directors/']

    rules = (
        #Rule(LinkExtractor(allow=r'/directors/page/\d+/$'), callback='parse', follow=True),
        Rule(LinkExtractor(allow=r'/directors/(?!page).*/$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = Director()
        name_and_role = response.xpath('//div[@class="main-info"]/p/text()').extract()[0].split(': ')
        name = name_and_role[1].split(' ')
        i['role'] = name_and_role[0]
        i['first_name'] = name[0]
        i['last_name'] = (' ').join(name[1:])

        i['phone_number'] = response.xpath('//div[@class="contact-left"]//p[contains(., "Phone:")]/text()').extract()[0].split(': ')[1]
        i['fax_number'] = response.xpath('//div[@class="contact-left"]//p[contains(., "Fax:")]/text()').extract()[0].split(': ')[1]
        i['email'] = response.xpath('//div[@class="contact-left"]//p[contains(., "Email:")]/a/text()').extract()[0]
        i['county'] = response.xpath('//div[@class="contact-right"]//p').extract()[1].strip().replace('<p>', '').replace('</p>', '') 

        return i
