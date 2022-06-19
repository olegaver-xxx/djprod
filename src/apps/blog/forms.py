from django import forms
from .models import Article
from django.contrib.auth.models import User


class ArticleForm(forms.ModelForm):

     class Meta:
         model = Article
         fields = '__all__'

class ArticleEditForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = 'title', 'text', 'published'