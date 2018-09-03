# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    user = models.TextField(db_column='user_id', max_length=40)
    hash = models.TextField(db_column='hash', max_length=1000)

class Post(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    url = models.URLField(db_column='url')
    image = models.TextField(db_column='image')
    desc = models.TextField(db_column='description', max_length=1000)
    likes = models.IntegerField(db_column='likes')
    dislikes = models.IntegerField(db_column='dislikes')
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.TextField(db_column='comment', max_length='500')
