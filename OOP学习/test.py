from models.objects import *

# 面向对象，构造器
# user1 = TUser(input('username:'), input('password:'))
# print(user1) # __str__
# if user1.getUsername()=='admin' and user1.getPassword()=='123456':
#     print(u'login successfully!')
# else:
#     print('fail')

# 方法重写
user1 = TUser('admin', '123', 170, 50)
# user1.run()

# 多态
seller = TSell(180, 70)
def getMethod(person):
    person.run()

getMethod(seller)
