# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from save_app.models import My_save_model


class MyscrapyItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    save_model = My_save_model
