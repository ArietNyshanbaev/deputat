from django.shortcuts import render
from custom_code.decorators import email_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from promis.models import Promis
from news.models import News
from forecast.models import Forecast
from django.db.models import Q
from django.core.context_processors import csrf

def main(request):
	# Инициализация переменных
	args = {}
	args['promises'] = Promis.objects.filter(is_approved=True)[:12]
	args['news'] = News.objects.all()[:6]
	args['forecasts'] = Forecast.objects.all()[:6]

	template = 'main/main.html'
	return render(request, template, args)

def search(request):
	# Инициализация переменных
	args = {}
	args.update(csrf(request))
	q = request.POST.get('q', '')
	results = Promis.objects.filter(Q(title__icontains=q) | Q(body__icontains=q) | Q(person__party__title__icontains=q)).filter(is_approved=True)
	args['promises'] = results
	template = 'main/search.html'
	return render(request, template, args)

