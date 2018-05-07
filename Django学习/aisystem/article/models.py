from django.db import models

# Create your models here.
class TArticle(models.Model):
    articleId = models.AutoField(primary_key=True, unique=True)
    articleName = models.CharField(max_length=200)
    articleContent = models.CharField(max_length=1000)
    articlePic = models.ImageField()
    dateCreated = models.DateTimeField()
    def __str__(self):
        articleNameJson = '"articleName":"'+str(self.articleName)+'",'
        articleIdJson = '"articleId":"' + str(self.articleId) + '",'
        articleContentJson = '"articleContent":"' + str(self.articleContent) +'"'
        return "{" + articleNameJson + articleIdJson + articleContentJson + "},"