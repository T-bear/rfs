from django.contrib.auth.models import User
from django import forms
from .models import Posts


from django import forms

class PostsAdd(forms.Form):
    titel = forms.CharField(label='titel', max_length=100)
    blog_post = forms.CharField(label='blog post', max_length=2500)

