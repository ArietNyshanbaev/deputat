from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', 'stopkadr.views.main', name='main'),
    url(r'^detailed_mediafile/(?P<file_id>.+)$', 'stopkadr.views.detailed_mediafile', name='detailed_mediafile'),
]