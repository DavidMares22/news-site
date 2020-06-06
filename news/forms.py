from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField( widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5
    }))
    photo = forms.ImageField()
    is_published = forms.BooleanField(initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))
