from django.db import models

# Create your models here.

# ORM 实体关系映射

# 模型简单来说就是类
# 一般都需要继承models.Model

# 实体类
class TUser(models.Model):
    userId = models.AutoField(primary_key=True, unique=True) # 自增，主键一般自增
    username = models.CharField(max_length=50) # 必须指定最大程度，默认varchar
    password = models.CharField(max_length=50)