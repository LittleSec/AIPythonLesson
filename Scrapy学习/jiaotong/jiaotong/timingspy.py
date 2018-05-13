import time
import os
while True:
    print("获取路况信息。。。")
    os.system("scrapy crawl lk")
    print("爬取结束！")
    time.sleep(60) # 一分钟爬一次