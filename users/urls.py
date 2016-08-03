from django.conf.urls import patterns, include, url

from rest_framework import routers
from rest_framework.authtoken import views

from users.views import AccountViewSet, MyAccount, GetUserByEmail, searchUser, clients

router = routers.DefaultRouter()
router.register(r'users', AccountViewSet, 'users')

urlpatterns = patterns('',
        url(r'^auth/', views.obtain_auth_token),
        url(r'myaccount/', MyAccount.as_view()),
        url(r'email/', GetUserByEmail.as_view()),
        url(r'clients/', clients),
        url(r'^users/search/(?P<keyword>\w+)/', searchUser.as_view()),
        url('^', include(router.urls)),
)
