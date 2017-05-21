from django.conf.urls import url

from . import views

app_name="Short"

urlpatterns = [
	url(r'^$',views.index,name="index"),
    url(r'^(?P<in_token>[0-9a-zA-Z]+)$', views.index,name="index"),
]