from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Article
from .forms import ArticleForm, ArticleEditForm


class IndexView(ListView):
    template_name = 'blog/article_list.html'
    model = Article
    context_object_name = 'articles'
    ordering = '-date'


class ArtView(DetailView):
    model = Article
    context_object_name = 'articles'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    template_name = 'blog/create.html'
    success_url = "/"

    def get_initial(self):
        return dict(
            author=self.request.user
        )


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'blog/create.html'
    model = Article
    form_class = ArticleEditForm
    success_url = "/"


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