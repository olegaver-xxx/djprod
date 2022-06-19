from django.shortcuts import render
from django.views.generic import  ListView, DetailView
from .models import Article

class IndexView(ListView):
    template_name = 'blog/article_list.html'
    model = Article
# def ViewHTML(request):
#     return render(request, 'article_list.html')


class ArtView(DetailView):
    model = Article

