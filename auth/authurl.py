__author__ = 'Dpak Malla'
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url(r'^$','auth.authview.Index',name='Index')
                       )