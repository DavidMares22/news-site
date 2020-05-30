from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='home'),
    path('category/<int:id>',get_category,name='detail')
]
