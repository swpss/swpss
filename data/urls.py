from django.conf.urls import url

from data import views

urlpatterns = [
        url(r'^data/(?P<m_id>\w+)/',
            views.DatasetView.as_view()),
        url(r'^chartData/(?P<m_id>\w+)/',
            views.chartDatasetView.as_view()),
        url(r'^insert/', views.DataInsert.as_view()),
        url(r'^recent/(?P<m_id>\w+)/',
            views.GetRecentData.as_view()),
        url(r'^range/(?P<m_id>\w+)/',
            views.DataWithRange.as_view()),
        url(r'^lpd/(?P<m_id>\w+)/',
            views.GetLPDData.as_view()),
        url(r'^pow/(?P<m_id>\w+)/',
            views.GetPowData.as_view()),
        url(r'^analysis/',
            views.GetLPDDataAnalysis.as_view()),
        url(r'^analysis1/',
            views.GetLPDDataAnalysis1.as_view()),
        url(r'^due_to/',
            views.faultAnalysis.as_view()),
        url(r'^status/',
            views.MachineStatus.as_view()),
]
