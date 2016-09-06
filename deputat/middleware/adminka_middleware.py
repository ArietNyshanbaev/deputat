from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib import messages

class AdminkaMiddleware(object):
	# Check if user has email
	def process_request(self, request):
		if '/adminka' in request.path_info:
			if request.user.is_authenticated():
				if not request.user.is_staff:
					request.path_info = reverse('main:main')
					messages.info(request, 'Вы не являетесь модератором.')
			else:
				request.path_info = reverse('main:main')
				messages.info(request, 'Вам нужно авторизоваться для совершения данноего действия')
		return None
