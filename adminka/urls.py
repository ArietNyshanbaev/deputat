from django.conf.urls import patterns, include, url

urlpatterns = [
	url(r'^$', 'adminka.views.main', name='main'),
    url(r'^deputats$', 'adminka.views.deputats', name='deputats'),
    url(r'^deputats/delete_deputat/(?P<deputat_id>.+)$', 'adminka.views.delete_deputat', name='delete_deputat'),
    url(r'^deputats/create_deputat$', 'adminka.views.create_deputat', name='create_deputat'),
    url(r'^deputats/edit_deputat/(?P<deputat_id>.+)$', 'adminka.views.edit_deputat', name='edit_deputat'),
    url(r'^users$', 'adminka.views.users', name='users'),
    url(r'^users/bann_user/(?P<user_id>.+)$', 'adminka.views.bann_user', name='bann_user'),

]
