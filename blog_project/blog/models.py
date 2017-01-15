#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    '''
    文章主体
    '''
    STATUS_CHOICES = (
            ('d', 'Draft'),
            ('p', 'Published'),
        )

    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('创建时间', auto_now=True)
    status = models.CharField('文章状态', max_length=1, choices = STATUS_CHOICES)
    abstract = models.CharField('摘要', max_length=54, blank=True, null=True, help_text='可选，如为空则取正文前54个字符')
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('喜欢', default=0)
    topped = models.BooleanField('置顶', default=False)
    category = models.ForeignKey('Category', verbose_name='分类', null=True, on_delete=models.SET_NULL)
    #on_delete=models.SET_NULL表示删除某个分类（category）后该分类下所有的Article的外键设为null（空）
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified_time']

class Category(models.Model):
    '''
    文章类型
    '''
    name = models.CharField('类型', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name



        