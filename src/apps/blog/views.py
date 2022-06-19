from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.views.generic import  ListView, DetailView, CreateView, UpdateView
from .models import Article
from .forms import ArticleForm, ArticleEditForm


class IndexView(ListView):
    template_name = 'blog/article_list.html'
    model = Article
    context_object_name = 'articles'
# def ViewHTML(request):
#     return render(request, 'article_list.html')

class ArtView(DetailView):
    model = Article
    context_object_name = 'articles'

class ArticleCreateView(CreateView):
    form_class = ArticleForm
    template_name = 'blog/create.html'
    success_url = "/"

class ArticleUpdateView(UpdateView):
    template_name = 'blog/create.html'
    model = Article
    form_class = ArticleEditForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('home'))
            success_url = "/"
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})