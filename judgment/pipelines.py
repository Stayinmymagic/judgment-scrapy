# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class AgeFilterPipeline:
    def process_item(self, item, spider):
        if item['event_age'] < 20:
            raise DropItem(f"年紀小於 20")
        return item

class DropDuplicatesPipeline:
    def __init__(self):
        self.article = set()
    def process_item(self, item, spider):
        link = item['link'] 
        if link in self.article:
            raise DropItem('duplicates link found %s', item)
        self.article.add(link)
        return item
class SavePipeline:
    def process_item(self, item, spider):
        item.save()
        print("save item")
        return item

# class SqlitePipeline:   
#     def open_spider(self, spider):
#         db_uri = spider.settings.get('MONGODB_URI', 'mongodb://localhost:27017')
#         db_name = spider.settings.get('MONGODB_DB_NAME', 'ptt_scrapy')
#         self.db_client = MongoClient('mongodb://localhost:27017')
#         self.db = self.db_client[db_name]

#     def process_item(self, item, spider):
#         self.insert_article(item)
#         return item

#     def insert_article(self, item):
#         item = dict(item)
#         self.db.article.insert_one(item)

#     def close_spider(self, spider):
#         self.db_clients.close()