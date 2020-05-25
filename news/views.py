from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    items = News.objects.all()
    return render(request,'news/index.html',{'items':items})
