from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', 'main.views.main', name='main'),
    url(r'^zhogorku_kenesh/(?P<party_id>.+)$', 'person.views.zhogorku_kenesh', name='zhogorku_kenesh'),
    url(r'^zhogorku_kenesh$', 'person.views.zhogorku_kenesh', name='zhogorku_kenesh'),
    url(r'^mestnyi_kenesh/(?P<region_id>.+)$', 'person.views.mestnyi_kenesh', name='mestnyi_kenesh'),
    url(r'^mestnyi_kenesh$', 'person.views.mestnyi_kenesh', name='mestnyi_kenesh'),
    url(r'^detailed_person/(?P<person_id>.+)$', 'person.views.detailed_person', name='detailed_person'),
]