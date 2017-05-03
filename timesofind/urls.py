from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.timesofind, name='TimesOfIndia_page'),
]
