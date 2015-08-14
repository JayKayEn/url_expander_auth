from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.url_list, name='url_list'),
    url(r'url/(?P<pk>[0-9]+)/$', views.url_detail, name='url_detail'),
    url(r'url/new/$', views.url_new, name='url_new'),
    url(r'url/remove/(?P<pk>[0-9]+)$', views.url_remove, name='url_remove'),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': 'url_list'}, name='logout'),
]
