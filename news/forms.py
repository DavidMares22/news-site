from django import forms
from .models import Category
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(help_text='at least 8 characters',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField( widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5
    }))
    photo = forms.ImageField()
    is_published = forms.BooleanField(initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d',title):
            raise ValidationError('title can not start with numbers')
        return title