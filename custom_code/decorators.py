from django.shortcuts import redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from auths.models import Verification

def email_required(f):
	def wrap(request, *args, **kwargs):
		if request.user.is_authenticated() and Verification.objects.filter(user=request.user).exists() and request.user.verification.is_verified == False:
			return redirect(reverse('auths:need_to_verify_email'))   
		return f(request, *args, **kwargs)
	wrap.__doc__=f.__doc__
	wrap.__name__=f.__name__
	return wrap

def logout_required(f):
	def wrap(request, *args, **kwargs):
		if request.user.is_authenticated() :
			return redirect(reverse('main:main')) 
		return f(request, *args, **kwargs)
	wrap.__doc__=f.__doc__
	wrap.__name__=f.__name__
	return wrap
