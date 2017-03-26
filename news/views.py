from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import ArchiveIndexView
from django.utils import timezone

from news.models import Article, Category


class ArticleIndexView(ArchiveIndexView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArchiveIndexView, self).get_context_data(**kwargs)
        return context



class ArticleListView(ListView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



class CategoryListView(ListView):

    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)        
        context['now'] = timezone.now()        
        return context

class ArticleDetailView(DetailView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    

   


