#
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search-result/$', views.search, name='search'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^about/$', views.about, name='about'),
]