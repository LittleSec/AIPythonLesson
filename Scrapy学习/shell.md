# scrapy相关命令

## 最简单的爬虫
1. 通过srapy shell爬虫，后面是url
    + ```scrapy shell http://www.baidu.com```
    + 之后会进行爬虫并进入srapy shell(相当于python shell)
2. 查看爬取的页面
    + ```view(response)```
    + 会打开爬取的页面（本地的）
3. 查看某元素的内容
    + ```response.xpath('//*[@id="u1"]/a[1]').extract()```
    + xpath里的参数是要查看的元素的xpath，要注意的是，这个xpath是爬取下来之后页面的xpath（如果不一样的话）
    + 这时打印的是html，包含标签的。下面才是打印不包含标签的内容。
    + ```response.xpath('//*[@id="u1"]/a[1]/text()').extract()```
    + 要注意字符串里单引号```'```和双引号```"```的问题


## 爬虫项目
1. 创建爬虫工程，工程名为jiaotong
```scrapy startproject jiaotong```
2. 运行爬虫，爬虫名为lk
```scrapy crawl lk```



