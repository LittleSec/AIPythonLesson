# python函数的学习
# 尤其是闭包，装饰器

'''
在库函数中常见到这种参数：
    *args是个元组
    *kvargs是个字典
实际上是一种装包和解包。
'''

'''
# 返回函数+闭包的特点：
1、嵌入函数
2、子函数调用父函数的变量
3、父函数返回子函数
'''
def valid(fun):
    def inner(*args): # 装包
        print('是否登录？')
        # *args # 解包
        fun(*args)
        print('录入日志...')
    return inner

@valid #装饰器
def apply(*args):
    # print("是否登录？")
    c = 0
    for i in args: # args是个元组
        c += i
    print("执行业务逻辑")
    # print("录入日志...")
    return c

@valid
def apply2(a, b):
    print("apply2...")

# valid(apply)(2, 3)
apply(2, 3) # 效果同上面写法
# apply2(1, 4)