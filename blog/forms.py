from django.contrib.auth.models import User
from django import forms
from .models import Posts, Profile
from ckeditor.widgets import CKEditorWidget

from django import forms

class PostsAdd(forms.Form):
    titel = forms.CharField(label='Titel', max_length=100)
    blog_post = forms.CharField(label='', widget=CKEditorWidget())

class ProfileChange(forms.Form):
    profile_pic = forms.CharField(label='', max_length=100)
    profile_info = forms.CharField(label='', widget=CKEditorWidget())


