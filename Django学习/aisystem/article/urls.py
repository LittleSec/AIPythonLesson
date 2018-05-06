# 本服务（app）的url映射，格式参照整个项目的urls.py映射
from django.urls import path
from . import views

urlpatterns = [
    path('/create', views.create), # 创建文章
    path('/all', views.all), # 显示所有文章
    path('', views.all)
]