from django.conf.urls import patterns, include, url

urlpatterns = [
	url(r'^$', 'adminka.views.main', name='main'),
    # Routes to deputats section of Adminka module
    url(r'^deputats$', 'adminka.views.deputats', name='deputats'),
    url(r'^deputats/delete_deputat/(?P<deputat_id>.+)$', 'adminka.views.delete_deputat', name='delete_deputat'),
    url(r'^deputats/create_deputat$', 'adminka.views.create_deputat', name='create_deputat'),
    url(r'^deputats/edit_deputat/(?P<deputat_id>.+)$', 'adminka.views.edit_deputat', name='edit_deputat'),
    # Routes to users section of Adminka module
    url(r'^users$', 'adminka.views.users', name='users'),
    url(r'^users/bann_user/(?P<user_id>.+)$', 'adminka.views.bann_user', name='bann_user'),
    url(r'^users/disbann_user/(?P<user_id>.+)$', 'adminka.views.disbann_user', name='disbann_user'),
    url(r'^users/delete_user/(?P<user_id>.+)$', 'adminka.views.delete_user', name='delete_user'),
    # Routes to news section of Adminka module
    url(r'^news$', 'adminka.views.news', name='news'),
    url(r'^news/delete_news/(?P<news_id>.+)$', 'adminka.views.delete_news', name='delete_news'),
    url(r'^news/create_news$', 'adminka.views.create_news', name='create_news'),
    url(r'^news/edit_news/(?P<news_id>.+)$', 'adminka.views.edit_news', name='edit_news'),
    # Routes to promises section of Adminka module
    url(r'^promises$', 'adminka.views.promises', name='promises'),
    url(r'^promises/delete_promis/(?P<promis_id>.+)$', 'adminka.views.delete_promis', name='delete_promis'),
    url(r'^promises/create_promis$', 'adminka.views.create_promis', name='create_promis'),
    url(r'^promises/edit_promis/(?P<promis_id>.+)$', 'adminka.views.edit_promis', name='edit_promis'),
]
