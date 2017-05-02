from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Posts( models.Model):
    auth_user = models.ForeignKey(User, on_delete=models.CASCADE,)
    title = models.CharField(max_length=50)
    blog_post = models.TextField()
    time_date = models.DateTimeField()
    blog_pic = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class Profile (models.Model):
    auth_user = models.ForeignKey(User, on_delete=models.CASCADE,)
    profile_info = models.TextField(max_length=2500)
    profile_pic = models.CharField(max_length=1000)

    def __str__(self):
        return self.profile_info