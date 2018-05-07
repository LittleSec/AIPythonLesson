# 迭代器和生成器的学习

'''
有时候如果直接用for等循环来做迭代的话，如果迭代数量很多，就会全部放入内存中，这样会很占用资源。
迭代器和生成器的作用就是解决这样的问题。
'''
# 迭代器
list = [4,5,6,7]
iter1 = iter(list) # 创建迭代器
print(next(iter1)) # 4

for i in iter1:
    print(i)

# 以下用法更节省内存资源
while True:
    try:
        print(next(iter1))
    except StopIteration:
        break
'''
其实有点类似于指针，iter1记录当前的位置，每次next后就改变当前‘指针’。
只能往前走，不能倒后。
无论是迭代器还是生成器，每次停下来只是记录当前的信息而不是全部内容。调用next()后就从当前位置开始执行。
所以如果上述代码完全不注释直接跑的话:
for循环打印的是5 6 7
while循环一进入就立刻抛出StopIteration而跳出循环。
'''

# 生成器
# 生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
i = 0
def fun():
    global i
    while i < 10:
        yield i # yield关键字只能在函数里定义
        # 每次生成i后就会暂停等待而不是继续while循环
        i += 1

funiter = fun() # 这就是为什么yield关键字只能在函数里定义
while True:
    try:
        print(next(funiter)) # 不能print(next(fun()))，这样等于每次都新生成一个生成器
    except StopIteration:
        break