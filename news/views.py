from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import News,Category

from .forms import *
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from django.contrib.auth import logout as do_logout
from django.core.mail import send_mail


def index(request):
    news = News.objects.all()
    paginator = Paginator(news, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(request.user)
    return render(request,'news/index.html',{'page_obj':page_obj})


def get_category(request,id):
    
    news = News.objects.filter(category_id = id)
    paginator = Paginator(news, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # category = Category.objects.get(pk=id)
    category = get_object_or_404(Category, pk=id)
    return render(request,'news/detail.html',{'category':category,'page_obj':page_obj})

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



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account succesfully created')
            return redirect('login')
        else:
            messages.error(request,'An error ocurred')
    else:
        form = RegisterForm()
    return render(request,'news/register.html',{'form':form})


def login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                do_login(request, user)       
                return redirect('home')

    return render(request,'news/login.html',{'form':form})



def logout(request):
    do_logout(request)
    return redirect('login')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'],form.cleaned_data['content'],'damr18@gmail.com',['damr18@gmail.com'],fail_silently=True)
            
            if mail:
                messages.success(request,'mail sent!')
            else:
                messages.error(request,'there was an error')
        else:
            messages.error(request,'there was an error')
    else:
        form = ContactForm()
    return render(request,'news/contact.html',{'form':form})