""" This is basically creating urls.py for the blo app and we also import
views and add one (post_list) of them in the urlpatterns"""

from django.conf.urls import url
from . import views

urlpatterns= [

      url(r'^$', views.post_list, name = 'post_list'),


]
