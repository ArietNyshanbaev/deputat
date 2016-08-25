from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^add_promis$', 'promis.views.add_promis', name='add_promis'),
    url(r'^add_result$', 'promis.views.add_result', name='add_result'),
    url(r'^detailed_promis/(?P<promis_id>.+)$', 'promis.views.detailed_promis', name='detailed_promis'),
    url(r'^new_promises$', 'promis.views.new_promises', name='new_promises'),
    url(r'^done_promises$', 'promis.views.done_promises', name='done_promises'),
    url(r'^not_done_promises$', 'promis.views.not_done_promises', name='not_done_promises'),
    url(r'^believe/(?P<promis_id>.+)$', 'promis.views.believe', name='believe'),
    url(r'^not_believe/(?P<promis_id>.+)$', 'promis.views.not_believe', name='not_believe'),
]