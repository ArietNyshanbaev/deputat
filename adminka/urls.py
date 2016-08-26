from django.conf.urls import patterns, include, url

urlpatterns = [
	url(r'^$', 'adminka.views.main', name='main'),
    url(r'^deputats$', 'adminka.views.deputats', name='deputats'),
    url(r'^delete_deputat/(?P<deputat_id>.+)$', 'adminka.views.delete_deputat', name='delete_deputat'),
]
