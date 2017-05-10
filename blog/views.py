from .models import Posts, Profile
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PostsAdd, ProfileChange
import datetime

#from .forms import NameForm

#shows users on the blog
def index(request):
    all_posts = User.objects.filter()
    return render(request, 'blog/index.html', {'all_posts': all_posts})

#shows all posts and filter it by users url.
def detail(request, auth_user_id):

    user = auth_user_id

    all_posts = Posts.objects.order_by('-time_date')
    all_posts = all_posts.filter(auth_user_id=user)

    profile_info = Profile.objects.all()
    profile_info = profile_info.filter(auth_user_id=user)

    matrix = [profile_info], [all_posts]

    return render(request, 'blog/detail.html', {'all_posts': all_posts, 'profile': profile_info})

def UserProfile(request,auth_user_id):

    profile_info = Profile.objects.all()
    user = auth_user_id
    profile_info = profile_info.filter(auth_user_id=user)
    return render(request, 'blog/profile.html', {'profile_info': profile_info})

def logout_view(request):
    logout(request)
    return HttpResponse('registration/login.html')


def get_name(request, auth_user_id):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostsAdd(request.POST)
        print(request.POST['titel'])
        print(request.POST['blog_post'])
        p = Posts(auth_user_id=auth_user_id, title=request.POST['titel'], blog_post=request.POST['blog_post'], time_date=datetime.datetime.now(), blog_pic="")
        p.save()
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/' + auth_user_id)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostsAdd()

    return render(request, 'blog/posts-add.html', {'form': form, 'id': auth_user_id})

def change_profile(request, auth_user_id):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfileChange(request.POST)
        print(request.POST['profile_pic'])
        print(request.POST['profile_info'])
        p = Profile(auth_user_id=auth_user_id, profile_pic=request.POST['profile_pic'], profile_info=request.POST['profile_info'])
        p._do_update(pk_val=auth_user_id, update_fields=['profile_pic' 'profile_info'])
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/' + auth_user_id)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfileChange()

    return render(request, 'blog/change_profile.html', {'form': form, 'id': auth_user_id})



























































