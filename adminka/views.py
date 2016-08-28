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
from promis.models import Promis, Result
from person.models import Person
from .forms import PersonForm, NewsForm, PromisForm
from news.models import News

def main(request):
	args = {}
	template = 'adminka/main.html'
	return render(request, template, args)

def deputats(request):
	args = {}
	args['deputats'] = Person.objects.all()
	template = 'adminka/deputats.html'
	return render(request, template, args)

def delete_deputat(request, deputat_id):
	args = {}
	deputat = get_object_or_404(Person, pk=deputat_id)
	name = deputat.first_name + ' ' + deputat.last_name
	deputat.delete()
	messages.info(request, 'Депутат ' + name + ' успешно удален. ')
	return redirect(reverse('adminka:deputats'))

def create_deputat(request):
	args = {}
	args.update(csrf(request))
	form = PersonForm()

	if request.POST:
		form = PersonForm(request.POST, request.FILES)
		if form.is_valid() :
			deputat = form.save()
			name = deputat.first_name + ' ' + deputat.last_name
			messages.info(request, 'Депутат ' + name + ' успешно создан. ')
			return redirect(reverse('adminka:deputats'))
	args['form'] = form
	template = 'adminka/create_deputat.html'
	return render(request, template, args)

def edit_deputat(request, deputat_id):
	args = {}
	args.update(csrf(request))
	instance = get_object_or_404(Person, id=deputat_id)
	if request.method == 'POST':
		form = PersonForm(request.POST, request.FILES, instance=instance)
		if form.is_valid() :
			deputat = form.save()
			name = deputat.first_name + ' ' + deputat.last_name
			messages.info(request, 'Депутат ' + name + ' успешно изменен. ')
			return redirect(reverse('person:detailed_person', kwargs={'person_id':deputat.id}))
	else:
		form = PersonForm(instance=instance)
	args['form'] = form
	template = 'adminka/create_deputat.html'
	return render(request, template, args)

def users(request):
	args = {}
	args['users'] = User.objects.all()
	template = 'adminka/users.html'
	return render(request, template, args)

def bann_user(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	user.is_active = False
	user.save()
	messages.info(request, 'Вы забанили пользователя ' + user.username)
	return redirect(reverse('adminka:users'))

def disbann_user(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	user.is_active = True
	user.save()
	messages.info(request, 'Вы разбанили пользователя ' + user.username)
	return redirect(reverse('adminka:users'))

def delete_user(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	name = user.username
	user.delete()
	messages.info(request, 'Вы удалили пользователя ' + name)
	return redirect(reverse('adminka:users'))

def news(request):
	args = {}
	args['newses'] = News.objects.all()
	template = 'adminka/news.html'
	return render(request, template, args)

def delete_news(request, news_id):
	news = get_object_or_404(News, id=news_id)
	title = news.title
	news.delete()
	messages.info(request, 'Вы удалили новость ' + title)
	template = 'adminka/delete_news.html'
	return redirect(reverse('adminka:news'))

def create_news(request):
	args = {}
	args.update(csrf(request))
	form = NewsForm()

	if request.POST:
		form = NewsForm(request.POST, request.FILES)
		if form.is_valid() :
			news = form.save()
			title = news.title
			messages.info(request, 'Новость ' + title + ' успешно создана. ')
			return redirect(reverse('adminka:news'))
	args['form'] = form
	template = 'adminka/create_news.html'
	return render(request, template, args)

def edit_news(request, news_id):
	args = {}
	args.update(csrf(request))
	instance = get_object_or_404(News, id=news_id)
	if request.method == 'POST':
		form = NewsForm(request.POST, request.FILES, instance=instance)
		if form.is_valid() :
			news = form.save()
			title = news.title
			messages.info(request, 'Новость ' + title + ' успешно изменен. ')
			return redirect(reverse('news:detailed_news', kwargs={'news_id':news.id}))
	else:
		form = NewsForm(instance=instance)
	args['form'] = form
	template = 'adminka/create_news.html'
	return render(request, template, args)

def promises(request):
	args = {}
	args['promises'] = Promis.objects.all()
	template = 'adminka/promises.html'
	return render(request, template, args)

def delete_promis(request, promis_id):
	promis = get_object_or_404(Promis, id=promis_id)
	title = promis.title
	promis.delete()
	messages.info(request, 'Вы удалили обещание ' + title)
	return redirect(reverse('adminka:promises'))

def create_promis(request):
	args = {}
	args.update(csrf(request))
	form = PromisForm()

	if request.POST:
		form = PromisForm(request.POST, request.FILES)
		if form.is_valid() :
			promis = form.save(commit=False)
			promis.user = request.user
			promis.save()
			title = promis.title
			messages.info(request, 'Обещание ' + title + ' успешно создана. ')
			return redirect(reverse('adminka:promises'))
	args['form'] = form
	template = 'adminka/create_promis.html'
	return render(request, template, args)

def edit_promis(request, promis_id):
	args = {}
	args.update(csrf(request))
	instance = get_object_or_404(Promis, id=promis_id)
	if request.method == 'POST':
		form = PromisForm(request.POST, request.FILES, instance=instance)
		if form.is_valid() :
			promis = form.save()
			title = promis.title
			messages.info(request, 'Обещание ' + title + ' успешно изменена. ')
			return redirect(reverse('promis:detailed_promis', kwargs={'promis_id':promis.id}))
	else:
		form = PromisForm(instance=instance)
	args['form'] = form
	template = 'adminka/create_promis.html'
	return render(request, template, args)
