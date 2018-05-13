# 路况蜘蛛

import scrapy
import json
from jiaotong.items import JiaotongItem
import re

class LkSplider(scrapy.Spider):
    name = 'lk' # 重写蜘蛛名
    allowed_domains = ['qdznjt.com'] # 要爬虫的域名
    start_urls = ['http://www.qdznjt.com/index/roadStatus'] # 当前这个借口已经弃用了，但还没删，而且能直接get
    def parse(self, response):
        obs = json.loads(response.body)
        '''
        [
            {
                "pubdate": "2018-05-12 15:13",
                "roadStatus": "东海路(燕儿岛路-福州路)交通拥堵",
                "num": 1
            },
            ...
        ]
        '''
        for ob in obs:
            item = JiaotongItem()
            item['date'] = ob['pubdate']
            content = ob['roadStatus'].replace('）', ')').replace('（', '(')
            item['road'] = content[:content.rindex(')')+1] # 最后一个')'
            item['des'] = content[content.rindex(')')+1:]
            yield item
        nextpage = "http://www.qdznjt.com/trafficIndex/getMoreAreaList?areaStatus=4&currentPageNum={page}"
        for i in range(2, 10):
            yield scrapy.Request(nextpage.format(page=str(i)), callback=self.parse2)

    def parse2(self, response):
        roads = response.xpath('//*[@id="r_border"]/div[2]/table/tr/td[1]/text()').extract()
        dates = response.xpath('//*[@id="r_border"]/div[2]/table/tr/td[6]/text()').extract()
        deses = response.xpath('//*[@id="r_border"]/div[2]/table/tr/td[5]/div/text()').extract()
        roadlist = []
        for road in roads:
            roadlist.append(''.join(re.findall('[\u4e00-\u9fa5]', road)))
        deslist = []
        for des in deses:
            deslist.append(''.join(re.findall('[\u4e00-\u9fa5]', des)))
        datelist = []
        for date in dates:
            datelist.append(''.join(re.findall(r'\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}', date)))
        for thedate, thedes, theroad in zip(datelist, deslist, roadlist):
            item = JiaotongItem()
            item['date'] = thedate
            item['des'] = thedes
            item['road'] = theroad
            yield item
