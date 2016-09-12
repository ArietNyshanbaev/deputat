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
    # Routes to forecast section of Adminka module
    url(r'^forecasts$', 'adminka.views.forecasts', name='forecasts'),
    url(r'^forecasts/delete_forecast/(?P<forecast_id>.+)$', 'adminka.views.delete_forecast', name='delete_forecast'),
    url(r'^forecasts/create_forecast$', 'adminka.views.create_forecast', name='create_forecast'),
    url(r'^forecasts/edit_forecast/(?P<forecast_id>.+)$', 'adminka.views.edit_forecast', name='edit_forecast'),
    # Routes to promises section of Adminka module
    url(r'^promises$', 'adminka.views.promises', name='promises'),
    url(r'^promises/delete_promis/(?P<promis_id>.+)$', 'adminka.views.delete_promis', name='delete_promis'),
    url(r'^promises/create_promis$', 'adminka.views.create_promis', name='create_promis'),
    url(r'^promises/edit_promis/(?P<promis_id>.+)$', 'adminka.views.edit_promis', name='edit_promis'),
    # Routes to comments of Promises section of Adminka module
    url(r'^comments_of_promis/(?P<promis_id>.+)$', 'adminka.views.comments_of_promis', name='comments_of_promis'),
    url(r'^results_of_promis/(?P<promis_id>.+)$', 'adminka.views.results_of_promis', name='results_of_promis'),
    url(r'^detailed_result/(?P<result_id>.+)$', 'adminka.views.detailed_result', name='detailed_result'),
    url(r'^delete_result/(?P<result_id>.+)$', 'adminka.views.delete_result', name='delete_result'),
    url(r'^approve_comment/(?P<comment_id>.+)$', 'adminka.views.approve_comment', name='approve_comment'),
    url(r'^disapprove_comment/(?P<comment_id>.+)$', 'adminka.views.disapprove_comment', name='disapprove_comment'),
    url(r'^delete_comment/(?P<comment_id>.+)$', 'adminka.views.delete_comment', name='delete_comment'),
    # Routes to comments of News section of Adminka module
    url(r'^comments_of_news/(?P<news_id>.+)$', 'adminka.views.comments_of_news', name='comments_of_news'),
    url(r'^approve_comment_news/(?P<comment_id>.+)$', 'adminka.views.approve_comment_news', name='approve_comment_news'),
    url(r'^disapprove_comment_news/(?P<comment_id>.+)$', 'adminka.views.disapprove_comment_news', name='disapprove_comment_news'),
    url(r'^delete_comment_news/(?P<comment_id>.+)$', 'adminka.views.delete_comment_news', name='delete_comment_news'),
    # Routes to comments of Forecast section of Adminka module
    url(r'^comments_of_forecast/(?P<forecast_id>.+)$', 'adminka.views.comments_of_forecast', name='comments_of_forecast'),
    url(r'^approve_comment_forecast/(?P<comment_id>.+)$', 'adminka.views.approve_comment_forecast', name='approve_comment_forecast'),
    url(r'^disapprove_comment_forecast/(?P<comment_id>.+)$', 'adminka.views.disapprove_comment_forecast', name='disapprove_comment_forecast'),
    url(r'^delete_comment_forecast/(?P<comment_id>.+)$', 'adminka.views.delete_comment_forecast', name='delete_comment_forecast'),
    # Routes to comments of Stop Kadr section of Adminka module
    url(r'^mediafiles$', 'adminka.views.mediafiles', name='mediafiles'),
    url(r'^mediafiles/delete_mediafile/(?P<file_id>.+)$', 'adminka.views.delete_mediafile', name='delete_mediafile'),
    url(r'^mediafiles/create_mediafile$', 'adminka.views.create_mediafile', name='create_mediafile'),
    url(r'^mediafiles/edit_mediafile/(?P<file_id>.+)$', 'adminka.views.edit_mediafile', name='edit_mediafile'),
]
