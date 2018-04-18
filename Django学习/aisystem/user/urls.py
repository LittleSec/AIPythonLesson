# 本服务（app）的url映射，格式参照整个项目的urls.py映射
from django.urls import path
from . import views

urlpatterns = [
    path('/index', views.index),
    path('/login', views.login)
]