from django.contrib import admin
from .models import News
from .models import Category
# Register your models here.



    


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category','is_published')
    list_editable = ('is_published',)
    


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
   

admin.site.register(News,NewsAdmin)
admin.site.register(Category,CategoryAdmin)