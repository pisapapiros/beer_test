from django.conf.urls import url

from apps.bar.views import ListBarView, CreateBarView, UpdateBarView, DetailBarView

urlpatterns = [

    url(r'^$', ListBarView.as_view(), name='list-bar'),
    url(r'create', CreateBarView.as_view(), name='create-bar'),
    url(r'update/(?P<pk>\d+)', UpdateBarView.as_view(), name='update-bar'),
    url(r'detail/(?P<pk>\d+)', DetailBarView.as_view(), name='detail-bar'),

]