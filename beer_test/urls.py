"""beer_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

from apps.beer.views import CreateBeerView, ListBeerView, UpdateBeerView, DetailBeerView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', ListBeerView.as_view(), name='list-beer'),
    url(r'list', ListBeerView.as_view(), name='list-beer'),
    url(r'create', CreateBeerView.as_view(), name='create-beer'),
    url(r'update/(?P<pk>\d+)', UpdateBeerView.as_view(), name='update-beer'),
    url(r'detail/(?P<pk>\d+)', DetailBeerView.as_view(), name='detail-beer'),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)