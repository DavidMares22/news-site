from django.shortcuts import render
from django.http import HttpResponse
from .models import News,Category


def index(request):
    items = News.objects.all()
    return render(request,'news/index.html',{'items':items})


def get_category(request,id):
    
    news = News.objects.filter(category_id = id)
    category = Category.objects.get(pk=id)
    return render(request,'news/detail.html',{'category':category,'news':news})