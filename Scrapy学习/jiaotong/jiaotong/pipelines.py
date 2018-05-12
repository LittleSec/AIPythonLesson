# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JiaotongPipeline(object):
    def process_item(self, item, spider):
        print(item['date'], item['road'], item['des'])
        return item
