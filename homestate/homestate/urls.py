from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/v1/person$', csrf_exempt(views.people)),
    url(r'^api/v1/action$', csrf_exempt(views.action)),
    url(r'^api/v1/automatable$', csrf_exempt(views.automatable)),
]