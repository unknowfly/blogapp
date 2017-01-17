from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from models import *
from django.http import HttpResponse

import markdown2
# Create your views here.

class IndexView(ListView):
    template_name = 'blog/index-p.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = Article.objects.filter(status = 'P')
        for article in article_list:
            article.body = markdown2.markdown(article.body)
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'

    pk_url_kwarg = 'article_id'

    def get_object(self):
        obj = super(ArticleDetailView, self).get_object()
        obj.body = markdown2.markdown(obj.body)
        return obj

class CategoryView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = Article.objects.filter(category=self.kwargs['cate_id'], status = 'P')
        for article in article_list:
            article.body = markdown2.markdown(article.body)
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(CategoryView, self).get_context_data(**kwargs)


def insertdata(self):
    i = 2
    while i < 100:
        passage = Article()
        passage.title = 'Passage' + str(i)
        passage.body = 'PPPPPPPPPPPPPPPPPPPPPPPP'
        passage.abstract = 'Passage' + str(i)
        passage.status = 'p'
        passage.save()
        i += 1
    return HttpResponse("<p>complete</p>")
