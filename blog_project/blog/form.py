#-*- coding: utf-8 -*-
from django import forms
from models import *

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment

        fields = ['user_name', 'user_email', 'body']

        widgets = {
            'user_name':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入昵称',
                'aria-describedy':'sizing-addonl'
                }),
            'user_email':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "请输入邮箱",
                'aria-describedby': "sizing-addon1",
            }),
            'body': forms.Textarea(attrs={'placeholder': '我来评两句~'})
        }