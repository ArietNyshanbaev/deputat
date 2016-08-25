from django.shortcuts import render, get_object_or_404
from custom_code.decorators import email_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from .models import News

def main(request):
	# Инициализация переменных
	args = {}
	args['news'] = News.objects.all()
	template = 'news/main.html'
	return render(request, template, args)

def detailed_news(request, news_id):
	# Инициализация переменных
	args = {}
	args['new'] = get_object_or_404(News, pk=news_id)
	template = 'news/detailed_news.html'
	return render(request, template, args)