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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

from beer_test.views import IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', IndexView.as_view(), name='index-view'),

    url(r'^bar/', include('apps.bar.urls')),
    url(r'^beer/', include('apps.beer.urls')),

    url(r'^upload/', include('fileupload.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)