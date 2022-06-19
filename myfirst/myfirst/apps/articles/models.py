from django.db import models

class Article(models.Model):
    article_title = models.CharField('название статьи', max_length=200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')

class Comment(models.Model):
    pass