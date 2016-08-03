from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from users.views import AccountViewSet


base_url = r'^api/v1/'
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'swps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(base_url, include('users.urls')),
    url(base_url, include('machines.urls')),
    url(base_url, include('data.urls')),
    url(base_url, include('support.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
