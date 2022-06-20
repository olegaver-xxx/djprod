from django import forms
from .models import Article
from django.contrib.auth.models import User


class ArticleForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=User.objects.all(),
                                    widget=forms.HiddenInput)

    class Meta:
        model = Article
        fields = '__all__'

class ArticleEditForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = 'title', 'text', 'published', 'image'