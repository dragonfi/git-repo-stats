from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^stats/(?P<repo_url>.*)', views.stats, name = 'stats'),
    url(r'^', views.index, name='index'),
]
