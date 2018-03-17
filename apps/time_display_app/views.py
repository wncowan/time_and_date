# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# from django.contrib import message
def index(request):
    context = {
    "time": strftime("%Y-%m-%d %H:%M %p", gmtime())    
    }
    return render(request, 'time_display_app/index.html', context)
# Create your views here.
