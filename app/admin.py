# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User, Comment, Post

from django.contrib import admin

# Register your models here.
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Post)
