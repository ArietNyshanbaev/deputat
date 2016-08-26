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
from .forms import PersonForm

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
			deputat = form.save(commit=False)
			photo = request.FILES.get('photo', '')
			deputat.photo = photo
			deputat.save()
			name = deputat.first_name + ' ' + deputat.last_name
			messages.info(request, 'Депутат ' + name + ' успешно удален. ')
			return redirect(reverse('adminka:deputats'))
	args['form'] = form
	template = 'adminka/create_deputat.html'
	return render(request, template, args)

def edit_deputat(request, deputat_id):
	args = {}
	args.update(csrf(request))
	instance = get_object_or_404(Person, id=deputat_id)
	if request.method == 'POST':
		form = PersonForm(data=request.POST, instance=instance)
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

def bann_user(request, user_id)
