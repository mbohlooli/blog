# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import *

from django.shortcuts import render

def index(request):
    posts = Post.objects.all()[::-1]
    url = 'http://localhost:8000/'
    global module
    module = 'home'
    return render(request, 'home.html', {'posts': posts, 'url': url, 'module': module})
