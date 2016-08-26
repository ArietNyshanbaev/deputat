from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', 'news.views.main', name='main'),
    url(r'^detailed_news/(?P<news_id>.+)$', 'news.views.detailed_news', name='detailed_news'),
]