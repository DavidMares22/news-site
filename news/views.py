from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News,Category



def index(request):
    news = News.objects.all()
    return render(request,'news/index.html',{'news':news})


def get_category(request,id):
    
    news = News.objects.filter(category_id = id)
    # category = Category.objects.get(pk=id)
    category = get_object_or_404(Category, pk=id)
    return render(request,'news/detail.html',{'category':category,'news':news})

def news_post(request,id):
    # news_post = News.objects.get(pk = id)
    news_post = get_object_or_404(News,pk=id)
    return render(request,'news/news_post.html',{'news_post':news_post})