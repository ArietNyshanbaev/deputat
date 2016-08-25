from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^signin$', 'auths.views.signin', name='signin'),
    url(r'^signup$', 'auths.views.signup', name='signup'),
    url(r'^signout$', 'auths.views.signout', name='signout'),
    url(r'^profile/change_password/$', 'auths.views.change_password', name='change_password'),
    url(r'^profile/$', 'auths.views.profile', name='profile'),
    url(r'^verify/(?P<random_string>.+)$', 'auths.views.verify', name='verify'),
    url(r'^need_to_verify_email/$', 'auths.views.need_to_verify_email', name='need_to_verify_email'),
    url(r'^resend_verification/$', 'auths.views.resend_verification', name='resend_verification'),
]
