from django.conf.urls import url

from support import views

urlpatterns = [
        url(r'^support/issues/$', views.IssueList.as_view()),
        url(r'^support/issues/(?P<issue_id>[0-9]+)/reasons/$',
            views.ReasonList.as_view()),
        url(r'^support/solutions/$', views.SolutionList.as_view()),
        url(r'^support/complaints/$', views.ComplaintList.as_view()),
        url(r'^support/complaints/(?P<pk>[0-9]+)/$',
            views.ComplaintDetail.as_view()),
        url(r'^support/service/(?P<m_id>\w+)/$',
            views.ServicePage.as_view()),
]
