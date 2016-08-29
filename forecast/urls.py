from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', 'forecast.views.main', name='main'),
    url(r'^detailed_forecast/(?P<forecast_id>.+)$', 'forecast.views.detailed_forecast', name='detailed_forecast'),
    url(r'^add_comment/(?P<forecast_id>.+)/(?P<comment_id>.+)$', 'forecast.views.add_comment', name='add_comment'),
    url(r'^add_comment/(?P<forecast_id>.+)$', 'forecast.views.add_comment', name='add_comment'),
]