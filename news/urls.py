from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='home'),
    path('category/<int:id>',get_category,name='category'),
    path('news/<int:id>',news_post,name='news_post'),
    path('add/', add_post,name='add_post')
]
