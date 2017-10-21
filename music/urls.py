from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/25/
    # The brackets group the characters string pattern so that it isn't read as separate items
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),
]
