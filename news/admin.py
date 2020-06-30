from django.contrib import admin
from .models import News
from .models import Category

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'
    


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'category','is_published')
    list_editable = ('is_published',)
    


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
   

admin.site.register(News,NewsAdmin)
admin.site.register(Category,CategoryAdmin)