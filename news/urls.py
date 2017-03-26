from django.conf.urls import url
from django.contrib import admin
from django.views.generic.dates import ArchiveIndexView
from news import views
from news.views import ArticleListView, ArticleDetailView, CategoryListView
from news.models import Article, Category


urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='article-list'),
    url(r'^(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
    url(r'^category/(?P<slug>[1-5]{1})/$', CategoryListView.as_view(), name='category-list'),
]