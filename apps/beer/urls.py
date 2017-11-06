from django.conf.urls import url

from apps.beer.views import ListBeerView, CreateBeerView, UpdateBeerView, DetailBeerView

urlpatterns = [

    url(r'^$', ListBeerView.as_view(), name='list-beer'),
    url(r'create', CreateBeerView.as_view(), name='create-beer'),
    url(r'update/(?P<pk>\d+)', UpdateBeerView.as_view(), name='update-beer'),
    url(r'detail/(?P<pk>\d+)', DetailBeerView.as_view(), name='detail-beer'),

]