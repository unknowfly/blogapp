from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^insertdata/$', views.insertdata, name='insertdata'),
    url(r'^blog/$', views.IndexView.as_view(), name='index'),
    url(r'^blog/article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^blog/category/(?P<cate_id>\d+)', views.CategoryView.as_view(), name='category'),
    url(r'^blog/tag/(?P<tag_id>\d+)', views.TagView.as_view(), name='tag')
]