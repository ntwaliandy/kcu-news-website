from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural =   "categories"
    def __str__(self):
        return self.category_name


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article_title = models.CharField(max_length=200)
    simple_heading = models.CharField(max_length=500)
    cover_photo = models.FileField()
    article_photo_1 = models.FileField()
    article_photo_2 = models.FileField()
    body = models.TextField(max_length=10000)
    Date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.article_title
        