from django.conf.urls import patterns, include, url

urlpatterns = [
	url(r'^$', 'adminka.views.main', name='main'),
    url(r'^deputats$', 'adminka.views.deputats', name='deputats'),
    url(r'^deputats/delete_deputat/(?P<deputat_id>.+)$', 'adminka.views.delete_deputat', name='delete_deputat'),
    url(r'^deputats/create_deputat$', 'adminka.views.create_deputat', name='create_deputat'),
    url(r'^deputats/edit_deputat/(?P<deputat_id>.+)$', 'adminka.views.edit_deputat', name='edit_deputat'),
    url(r'^users$', 'adminka.views.users', name='users'),
    url(r'^users/bann_user/(?P<user_id>.+)$', 'adminka.views.bann_user', name='bann_user'),
    url(r'^users/disbann_user/(?P<user_id>.+)$', 'adminka.views.disbann_user', name='disbann_user'),
    url(r'^users/delete_user/(?P<user_id>.+)$', 'adminka.views.delete_user', name='delete_user'),
]
