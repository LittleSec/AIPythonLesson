# 表单型post
# 下面爬取的是aisystem的登录页面，其中验证码统一用123，并给login方法设置成接口
# 代码并未在本机测试过。

import scrapy

class LoginSplider(scrapy.Spider):
    name = 'ls'
    def start_requests(self):
        url = 'http://127.0.0.1:8000/user/login'
        yield scrapy.FormRequest(
            url = url,
            formdata = { # 下面都需要根据实际情况修改
                "username": "admin",
                "password": "123456",
                "code": "123", # 根据需要改
                "csrftoken": "", # 从cookie获取
                "sessionid": "" # 同上
            },
            callback = self.parse_pge
        )
    
    def parse_pge(self, response):
        print("_________________________________")
        print(response.body)