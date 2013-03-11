from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url(r'^', include('home.homeurl', namespace='Home')),
                       url(r'login/', include('auth.authurl', namespace='Auth')),
                       )
