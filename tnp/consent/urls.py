from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login_user, name='login_user'),
    url(r'^home', views.home, name='home'),
    url(r'^apply', views.apply, name='apply'),
    url(r'^cancel', views.cancel, name='cancel'),
    url(r'^logout/$', views.user_logout, name='logout'),
]
