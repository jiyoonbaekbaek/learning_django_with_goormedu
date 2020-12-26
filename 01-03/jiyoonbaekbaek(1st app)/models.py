from django.db import models

# Create your models here.
## python manage.py startapp posts (앱생성하기)

## posts 앱 안의 models.py

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    view_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

## settings.py 에서 INSTALLED_APPS 에 'posts' 추가하기!