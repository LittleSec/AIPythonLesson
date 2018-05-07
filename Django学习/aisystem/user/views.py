# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect  # 跳转路径的包
from .models import TUser
import random  # 生成随机色
from PIL import Image, ImageDraw, ImageFont
import io


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
    return render(request, 'index.html', {
        'mes': request.GET.get('mes'),
        'user': users
    })  # 重定向


def login(request):
    '''
    用户的登录
    '''
    if request.method == 'POST':
        username = request.POST.get("username")  # same with input tag name
        password = request.POST.get("password")
        code = request.POST.get("code")
        if code != request.session["code"]:
            return HttpResponseRedirect('login?mes=验证码不正确！')            
        # 模拟数据库查询操作
        # TUser.objects.get(username=username, password=password) # 若没有则会报错
        # 以下是过滤器
        if TUser.objects.filter(
                username=username, password=password).exists() == True:
            # if username == 'admin' and password == '123456':
            # return HttpResponse('登录成功！')
            request.session["username"] = username
            return HttpResponseRedirect('/')  # 重定向到显示所有文章的页面
        else:
            # return HttpResponse('登录失败！')
            return HttpResponseRedirect('login?mes=账号或密码错误！')
    else:
        mes = ''
        if request.GET.get('mes'):
            mes = request.GET.get('mes')
        return render(request, 'login.html', {'mes': mes})


def loginout(request):
    del request.session['username']
    return HttpResponseRedirect('/')


def code(request):
    width = 100
    height = 50
    size = (width, height)
    bg_color = (random.randrange(20, 100), random.randrange(20, 100),
                random.randrange(20, 100))
    img = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(img)
    for i in range(100): # 画些点做干扰
        point_position = (random.randrange(0, width),
                          random.randrange(0, height))  # 位置
        point_color = (random.randrange(0, 255), 255, random.randrange(0, 255)) # 颜色
        draw.point(point_position, fill=point_color)
    
    chars = []
    for i in range(48,58): #数字
        chars.append(chr(i))
    for i in range(97,123): #小写字母
        chars.append(chr(i))
    for i in range(65,91): #大写字母
        chars.append(chr(i))
    code_str = ''
    for i in range(4):
        code_str += chars[random.randrange(0, len(chars))]
    request.session["code"] = code_str
    font_family = ImageFont.truetype('/System/Library/Fonts/Noteworthy.ttc', 40)
    font_color = (255, random.randrange(0,255), random.randrange(0,255))
    for i in range(4): # 位置和字体有关
        draw.text((25*i , -5), text=code_str[i], font=font_family,fill=font_color)

    del draw
    buf = io.BytesIO()
    img.save(buf,'png')
    return HttpResponse(buf.getvalue(), 'image/png')