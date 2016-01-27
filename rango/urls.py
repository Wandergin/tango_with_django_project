from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'rango^$', views.index, name='index'))