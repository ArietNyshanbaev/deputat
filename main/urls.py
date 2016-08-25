from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', 'main.views.main', name='main'),
    url(r'^test$', 'main.views.test', name='test'),
]