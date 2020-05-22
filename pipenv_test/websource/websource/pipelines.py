# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from websource.dbmgr import DB


class WebsourcePipeline(object):
    url = ''

    def __init__(self):
        self.db = DB('websource.db')
        args = {
            'addr': "NVARCHAR(10) DEFAULT ''",
            'code': "NVARCHAR(10) DEFAULT ''",
        }
        self.db.create_table('web_1_test_1', args)
        self.db.commit_sql()

    def process_item(self, item, spider):
        sql = "INSERT INTO web_1_test_1 (addr, code) values ('%s', '%s')"
        self.db.execute_sql(sql % (item['addr'], item['code']))
        self.db.commit_sql()
        return item
