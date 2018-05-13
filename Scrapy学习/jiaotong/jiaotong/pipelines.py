# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy.crawler import Settings as settings

class JiaotongPipeline(object):
    def __init__(self, connect):
        self.connect = connect
        self.cursor = connect.cursor()

    @classmethod
    def from_settings(clazz, settings):
        connect = pymysql.connect(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            charset='utf8',
            use_unicode=True
        )
        return clazz(connect)

    def process_item(self, item, spider):
        # print(item['date'], item['road'], item['des'])
        # 去重
        selectsql = "select * from article_tarticle a where a.articlename='{road}' and a.articlecontent='{des}' and a.datecreated='{date}'".format(
            road=item['road'], des=item['des'], date=item['date']
        )
        self.cursor.execute(selectsql)
        if self.cursor.fetchone():
            pass
        else:
            # insert
            sql = "insert into article_tarticle(articlename, articlecontent, datecreated) values ('{road}', '{des}', '{date}')".format(
                road=item['road'], des=item['des'], date=item['date']
            )
            self.cursor.execute(sql)
            self.connect.commit()
        return item
