# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
    # define the fields for your item here like:
    source_url = scrapy.Field()
    head_title = scrapy.Field()
    head_meta = scrapy.Field()
    body_name = scrapy.Field()
    body_desc = scrapy.Field()
    body_content = scrapy.Field()
    pass
