from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/<album_id>/
    # The brackets group the characters string pattern so that it isn't read as separate items
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),

    # /music/album/add/
    url(r'^album/add/$', views.AlbumCreate.as_view(), name="create_album"),

    # /music/album/2/
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name="update_album"),

    # /music/album/2/delete/
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name="delete_album"),
]
