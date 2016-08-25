# pythone packages imports
from __future__ import unicode_literals
import re
# django core packages imports 
from django.shortcuts import redirect, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse , reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.conf import settings
from custom_code.decorators import email_required, logout_required
# import of custom writen decorator and views
from .models import Domain, Verification
from promis.models import Promis, Result

@logout_required
def signin(request, key='main'):
	# initialize variables
	args={}
	args.update(csrf(request))

	if request.GET.get('next', ''):
		messages.info(request, 'Чтобы совершить данное действие вам нужно авторизоваться. ')

	if request.POST:
		username = request.POST.get('login_or_email', '')
		password = request.POST.get('password', '')

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				# check if we got next value
				next_link = request.POST.get('next', '')
				if next_link != '' :
					return redirect(next_link)
				return redirect(reverse('main:main'))
			else:
				return redirect(request.META.get('HTTP_REFERER')+'?error=signin&note=Ваш аккаунт временно заблокирован.'+'&username='+username)
		else:
			return redirect(request.META.get('HTTP_REFERER')+'?error=signin&note=Имя пользователя и пароль не совпадают, попробуйте еще раз.'+'&username='+username)

	return redirect(reverse('main:main'))

@logout_required
def signup(request):
	# initialize variables
	args={}
	args.update(csrf(request))

	if request.POST:
		email = request.POST.get('email','')
		password = request.POST.get('password','')
		username = request.POST.get('username','')
		# Validation of Username and Email
		if User.objects.filter(username=username).exists():
			return redirect(request.META.get('HTTP_REFERER')+'?error=signup&note=Этот Логин уже используется, выберите другой Логин.&email='+email+'&username='+username)
		if User.objects.filter(email=email).exists():
			return redirect(request.META.get('HTTP_REFERER')+'?error=signup&note=Этот Email уже используется, выберите другой Email.&email='+email+'&username='+username)

		user = User.objects.create_user(username=username, email=email, password=password)
		user.save()
		random_string = get_random_string(length=32)
		verification = Verification.objects.create(user=user, random_string=random_string)
		try :
			domain_name = Domain.objects.all()[0]
		except :
			pass
		send_mail('Депутат КГ Email .' ,'Здравствуйте  ' + 'подтвердите ваш email пройдя по ссылке ' + 
		domain_name.domain +'/auths/verify/'+ random_string ,
		settings.EMAIL_HOST_USER, [email], fail_silently=True)
		# authenticate and login user
		user_login = authenticate(username=username, password=password)
		login(request, user_login)
		return redirect(reverse('auths:need_to_verify_email'))

	return redirect(reverse('main:main'))

@login_required(login_url=reverse_lazy('main:main'))
def signout(request):
	logout(request)

	return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url=reverse_lazy('auths:signin'))
def profile(request):
	# initialize variables
	args = {}
	args['promises'] = Promis.objects.filter(user=request.user, is_approved=True).count()
	args['results'] = Result.objects.filter(user=request.user).count()
	return render(request, 'auths/profile.html', args)


@login_required(login_url=reverse_lazy('auths:signin'))
def modify_profile(request):
	# initialize variables
	args = {}
	args.update(csrf(request))
	need_for_every(args,request)

	if request.POST:
		user = request.user 
		first_name = request.POST.get('first_name', '')
		user.first_name = first_name
		user.save()
		messages.info(request, 'Ваш аккаунт успешно отредактирован.')
		return redirect(reverse('auths:profile'))
	return render(request, 'auths/modify_profile.html', args)

@login_required(login_url=reverse_lazy('auths:signin'))
def change_password(request):
	args = {}
	args.update(csrf(request))
	user = request.user

	if request.POST:
		password_old = request.POST.get('password_old', '')
		password_new = request.POST.get('password_new', '')
		password_new1 = request.POST.get('password_new1', '')
		print password_old
		if request.user.check_password(password_old):
			if password_new == password_new1:
				user.set_password(password_new)
				user.save()
				messages.success(request, 'Ваш пароль успешно изменен, войдите заново используя новый пароль.')
			else:
				return redirect(request.META.get('HTTP_REFERER')+'?error=change_password&note=Ваши новые пароли не совпадают.')
		else:
			return redirect(request.META.get('HTTP_REFERER')+'?error=change_password&note=Вы ввели неправильный нынешний пароль.')
	return redirect(reverse('main:main')+'?error=signin')

def verify(request, random_string):
	args = {}
	args.update(csrf(request))
	verification = Verification.objects.filter(random_string=random_string)
	if verification.exists() and random_string != '':
		verification = verification[0]
		verification.is_verified = True
		verification.random_string = ''
		verification.save()
		messages.info(request, 'Поздравляем вы успешно подтвердили ваш email. ')
	else:
		messages.error(request, 'Данная ссылка не активна')
	return redirect(reverse('auths:signin'))

@login_required(login_url=reverse_lazy('auths:signin'))
def need_to_verify_email(request):
	if Verification.objects.filter(user=request.user).exists() and request.user.verification.is_verified == True:
		return redirect(reverse('main:main'))
	return render(request, 'auths/need_to_verify_email.html', {})

@login_required(login_url=reverse_lazy('auths:signin'))
def resend_verification(request):
	if Verification.objects.filter(user=request.user).exists() and request.user.verification.is_verified == True:
		return redirect(reverse('main:main'))
	verification = Verification.objects.filter(user=request.user)[0]
	try :
		domain_name = Domain.objects.all()[0]
	except :
		pass
	send_mail('Депутат КГ Email .' ,'Здравствуйте  ' + 'подтвердите ваш email пройдя по ссылке ' + 
	domain_name.domain +'/auths/verify/'+ verification.random_string ,
	settings.EMAIL_HOST_USER, [request.user.email], fail_silently=True)
	messages.info(request, 'Мы переотправили на вашу почту ссылку для подтверждения, проверьте почту, если не пришло проверьте папку со спамом.')
	return redirect(request.META.get('HTTP_REFERER'))
