from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.thehindu, name='TheHindu_page'),
]
