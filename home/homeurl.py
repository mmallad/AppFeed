__author__ = 'Dipak Malla'
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$','home.homeview.Home',name='Home'),
                       url(r'^accessID/$','home.homeview.AccessIDCall',name='AccessID'),
                       url(r'^pro/$','home.homeview.Procedure',name='Procedure'),
                       url(r'^feed/$','home.homeview.Feed',name='Feed')
                       )