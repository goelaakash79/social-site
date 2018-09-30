# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User, Comment, Post
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json

def login(request):
    msg = ''
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        password = data['hash'][::-1] + str(len(data['hash']) * 13)
        query = User.objects.create(user = data['user'], hash = password)
        msg = 'success'
    elif request.method == 'GET':
        msg = 'error'
    return JsonResponse({'data':msg}, safe=False)

def add_post(request):
    msg = ''
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        query = Post.objects.create(user = User.objects.get(user = data['user']), url = data['url'], image = data['image'], desc = data['desc'], likes=0, dislikes=0)
        msg = 'success'
    elif request.method == 'GET':
        msg = 'failure'
    return JsonResponse({'data': msg})

def get_posts(request):
    if request.method == 'GET':
        query = Post.objects.values('id','url','image','desc','likes','dislikes','user__user','user','created_at')
        x = list(query)
        x = x[::-1]
    return JsonResponse({"data": x})

def like(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        q = Post.objects.filter(id=data['id']).values('likes')
        likes = q[0]['likes'] + data['likes']
        query = Post.objects.filter(id = data['id']).update(likes=likes)
    return JsonResponse({"data": "success"})

def dislike(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        q = Post.objects.filter(id=data['id']).values('dislikes')
        dilikes = q[0]['dislikes'] + data['dislikes']
        query = Post.objects.filter(id = data['id']).update(dislikes=dislikes)
    return JsonResponse({"data": "success"})
