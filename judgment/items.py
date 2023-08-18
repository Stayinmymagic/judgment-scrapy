# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from webscraper.models import Judge
from scrapy_djangoitem import DjangoItem

class JudgmentItem(DjangoItem):
    django_model = Judge

