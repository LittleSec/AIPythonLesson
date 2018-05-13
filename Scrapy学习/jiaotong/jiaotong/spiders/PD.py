# 爬取苏宁MacPro价格的测试
# 需要用到selenium里的webdriver模拟浏览器行为
# 经分析苏宁网页的价格是ajax通过get请求得来的
import scrapy
from selenium import webdriver
import time

class PDSplider(scrapy.Spider):
    name = 'pd'
    allowed_domains= ['suning.com']
    start_urls = ['http://product.suning.com/0000000000/627657477.html']
    def parse(self, response):
        browser = webdriver.Chrome(executable_path='../chromedriver')
        browser.get(self.start_urls[0])
        time.sleep(2)
        price = browser.find_element_by_class_name('mainprice')
        print('______________________________________________')
        print(price.text)