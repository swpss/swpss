from django.conf.urls import patterns, include, url

from rest_framework import routers

from machines import views

router = routers.DefaultRouter()
router.register(r'models', views.MachineDetailsViewSet)
router.register(r'machines', views.MachineViewSet, 'machines')

urlpatterns = patterns('',
        url('^', include(router.urls)),
        # url('^machine-detail/', views.GetMachineDetails.as_view()),
          url(r'^status/', views.MachineStatus.as_view()),
)
