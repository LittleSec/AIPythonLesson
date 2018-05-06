from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import TArticle
import time, random, datetime
from django.conf import settings # 用户获取上传路径，在项目的setting.py里
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def create(request):
    if request.method == 'POST':
        articleName = request.POST.get('articleName')
        articleContent = request.POST.get("articleContent")
        files = request.FILES.getlist("articlePic")
        article = TArticle()
        if articleName:
            article.articleName = articleName
        if articleContent:
            article.articleContent = articleContent
        if len(files) > 0:
            article.articlePic = upload(files[0])
        article.dateCreated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        article.save()
        return HttpResponseRedirect('/article/all')
    else:
        return render(request, "create.html", {})

@csrf_exempt # 需要import，类似于api
def all(request):
    # 问题是如果每个登录都这样写的话，很繁琐，不利于开发，所以引入中间件，setting.py里的middleware
    # if 'username' not in request.session or not request.session["username"]:
    #     return HttpResponseRedirect("/user/login")
    if request.method == 'POST':
        articles = TArticle.objects.all() # ORM
        # articles = TArticle.objects.raw("select * from article_tarticle") # sql语句
        res = r'{"articlelist": ['
        for art in articles:
            res += str(art) # 在model里有重载
        return HttpResponse(res[:-1] + ']}') #最后一个逗号要去掉
    else:
        return render(request, "all.html", {})

def upload(file):
    fileType = file.name[file.name.rindex('.'):] # 最后一个点后面的就是文件类型，也可以.split('.')[-1]
    fileName = str(time.time()) + str(random.randrange(1000,10000)) + fileType
    myfile = open(settings.UPLOAD_PATH + '/' + fileName, 'wb')
    for i in file.chunks():
        myfile.write(i)
    myfile.close()
    return fileName