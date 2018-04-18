# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect # 跳转路径的包
from .models import TUser

def index(request):
    '''
    用户主页
    '''
    # 使用ORM访问数据库

    # 获取收据
    # users = TUser.objects.all() # 获取所有user

    # 插入数据
    # user = TUser()
    # user.username = 'xiaogang'
    # user.password = '123'
    # user.save() # 插入数据

    # 更新（改）数据
    # user = TUser.objects.get(username='xiaogang')
    # user.password = '123456'
    # user.save() # 更新数据（不用update）

    # 使用sql
    users = TUser.objects.raw('select * from user_tuser')

    # return HttpResponse('hello world!')
    return render(request, 'index.html', {'mes': request.GET.get('mes'), 'user': users}) # 重定向

def login(request):
    '''
    用户的登录
    '''
    if request.method == 'POST':
        username = request.POST.get("username") # same with input tag name
        password = request.POST.get("password")
        # 模拟数据库查询操作
        # TUser.objects.get(username=username, password=password) # 若没有则会报错
        # 以下是过滤器
        if TUser.objects.filter(username=username, password=password).exists() == True:
        # if username == 'admin' and password == '123456':
            # return HttpResponse('登录成功！')
            return HttpResponseRedirect('index?mes=登录成功！')
        else:
            # return HttpResponse('登录失败！')
            return HttpResponseRedirect('login?mes=账号或密码错误！')
    else:
        mes = ''
        if request.GET.get('mes'):
            mes = request.GET.get('mes')
        return render(request, 'login.html', {'mes': mes})