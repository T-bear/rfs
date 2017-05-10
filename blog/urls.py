from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #/blog/

    url(r'^(?P<auth_user_id>[0-9]+)', views.detail, name='detail'),
    # /blog/0-9/

    url(r'^login/', auth_views.login, name='login'),
    #/blog/login.

    url(r'^logout/', auth_views.logout, {'next_page': '/blog/'}, name='logout'),
    #blog/login, after logout it redirects back to the loginpage.

    url(r'^profile/(?P<auth_user_id>[0-9]+)', views.UserProfile, name='profile'),
    #/detail

    url(r'^admin/', admin.site.urls),

    url(r'^posts-add/(?P<auth_user_id>[0-9]+)', views.get_name, name='posts-add'),

    url(r'^change_profile/(?P<auth_user_id>[0-9]+)', views.change_profile, name='change_profile'),
]