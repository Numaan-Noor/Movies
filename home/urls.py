from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('', index, name='index'),
    path('all', all, name='all'),
    url(r'^download_board/(?P<pk>[0-9]+)/$', download_board, name='download_board'),
    url(r'^final/(?P<pk>[0-9]+)/$', final, name='final'),
    ]