from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import News,Category

from .forms import NewsForm
from django.core.paginator import Paginator



def index(request):
    news = News.objects.all()
    paginator = Paginator(news, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # print(request.user)
    return render(request,'news/index.html',{'page_obj':page_obj})


def get_category(request,id):
    
    news = News.objects.filter(category_id = id)
    # category = Category.objects.get(pk=id)
    category = get_object_or_404(Category, pk=id)
    return render(request,'news/detail.html',{'category':category,'news':news})

def news_post(request,id):
    # news_post = News.objects.get(pk = id)
    news_post = get_object_or_404(News,pk=id)
    return render(request,'news/news_post.html',{'news_post':news_post})

def add_post(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            n = News(title=cd['title'],content=cd['content'],is_published=cd['is_published'],photo=cd['photo'],category=cd['category'])
            n.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = NewsForm()
    return render(request, 'news/add_post.html', {'form': form})