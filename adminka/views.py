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
from promis.models import Promis, Result, Comments
from person.models import Person
from .forms import PersonForm, NewsForm, PromisForm, ForecastForm, MediaFileForm
from news.models import News, NewsComment
from forecast.models import Forecast, ForecastComment
from stopkadr.models import MediaFile

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

def forecasts(request):
	args = {}
	args['forecasts'] = Forecast.objects.all()
	template = 'adminka/forecasts.html'
	return render(request, template, args)

def delete_forecast(request, forecast_id):
	forecast = get_object_or_404(Forecast, id=forecast_id)
	title = forecast.title
	forecast.delete()
	messages.info(request, 'Вы удалили мнение ' + title)
	return redirect(reverse('adminka:forecasts'))

def create_forecast(request):
	args = {}
	args.update(csrf(request))
	form = ForecastForm()

	if request.POST:
		form = ForecastForm(request.POST, request.FILES)
		if form.is_valid() :
			forecast = form.save(commit=False)
			forecast.user = request.user
			forecast.save()
			title = forecast.title
			messages.info(request, 'Мнение ' + title + ' успешно создана. ')
			return redirect(reverse('adminka:forecasts'))
	args['form'] = form
	template = 'adminka/create_forecast.html'
	return render(request, template, args)

def edit_forecast(request, forecast_id):
	args = {}
	args.update(csrf(request))
	instance = get_object_or_404(Forecast, id=forecast_id)
	if request.method == 'POST':
		form = ForecastForm(request.POST, request.FILES, instance=instance)
		if form.is_valid() :
			forecast = form.save()
			title = forecast.title
			messages.info(request, 'Новость ' + title + ' успешно изменен. ')
			return redirect(reverse('forecast:detailed_forecast', kwargs={'forecast_id':forecast.id}))
	else:
		form = ForecastForm(instance=instance)
	args['form'] = form
	template = 'adminka/create_forecast.html'
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

def comments_of_promis(request, promis_id):
	args = {}
	promis = get_object_or_404(Promis, pk=promis_id)
	args['comments'] = Comments.objects.filter(promis=promis)
	template = 'adminka/comments_of_promis.html'
	return render(request, template, args)

def results_of_promis(request, promis_id):
	args = {}
	promis = get_object_or_404(Promis, pk=promis_id)
	args['results'] = Result.objects.filter(promis=promis)
	template = 'adminka/results_of_promis.html'
	return render(request, template, args)

def detailed_result(request, result_id):
	args = {}
	args['result'] = get_object_or_404(Result, id=result_id)
	template = 'adminka/detailed_result.html'
	return render(request, template, args)

def delete_result(request, result_id):
	result = get_object_or_404(Result, id=result_id)
	promis_id = result.promis.id
	result.delete()
	messages.info(request, 'Вы удалили данный итог. ')
	return redirect(reverse('adminka:results_of_promis', kwargs={'promis_id': promis_id}))

def approve_comment(request, comment_id):
	comment = get_object_or_404(Comments, pk=comment_id)
	comment.is_approved = True
	comment.save()
	messages.info(request, 'Вы подтвердили комент : ' + comment.content[:15])
	return redirect(reverse('adminka:comments_of_promis', kwargs={'promis_id': comment.promis.id}))

def disapprove_comment(request, comment_id):
	comment = get_object_or_404(Comments, pk=comment_id)
	comment.is_approved = False
	comment.save()
	messages.info(request, 'Вы скрыли комент : ' + comment.content[:15])
	return redirect(reverse('adminka:comments_of_promis', kwargs={'promis_id': comment.promis.id}))

def delete_comment(request, comment_id):
	comment = get_object_or_404(Comments, pk=comment_id)
	content = comment.content
	promis_id = comment.promis.id
	comment.delete()
	messages.info(request, 'Вы удалили комент : ' + content[:15])
	return redirect(reverse('adminka:comments_of_promis', kwargs={'promis_id': promis_id}))


def comments_of_news(request, news_id):
	args = {}
	news = get_object_or_404(News, pk=news_id)
	args['comments'] = NewsComment.objects.filter(news=news)
	template = 'adminka/comments_of_news.html'
	return render(request, template, args)

def approve_comment_news(request, comment_id):
	comment = get_object_or_404(NewsComment, pk=comment_id)
	comment.is_approved = True
	comment.save()
	messages.info(request, 'Вы подтвердили комент : ' + comment.content[:15])
	return redirect(reverse('adminka:comments_of_news', kwargs={'news_id': comment.news.id}))

def disapprove_comment_news(request, comment_id):
	comment = get_object_or_404(NewsComment, pk=comment_id)
	comment.is_approved = False
	comment.save()
	messages.info(request, 'Вы скрыли комент : ' + comment.content[:15])
	return redirect(reverse('adminka:comments_of_news', kwargs={'news_id': comment.news.id}))

def delete_comment_news(request, comment_id):
	comment = get_object_or_404(NewsComment, pk=comment_id)
	content = comment.content
	news_id = comment.news.id
	comment.delete()
	messages.info(request, 'Вы удалили комент : ' + content[:15])
	return redirect(reverse('adminka:comments_of_news', kwargs={'news_id': news_id}))


def comments_of_forecast(request, forecast_id):
	args = {}
	forecast = get_object_or_404(Forecast, pk=forecast_id)
	args['comments'] = ForecastComment.objects.filter(forecast=forecast)
	template = 'adminka/comments_of_forecast.html'
	return render(request, template, args)

def approve_comment_forecast(request, comment_id):
	comment = get_object_or_404(ForecastComment, pk=comment_id)
	comment.is_approved = True
	comment.save()
	messages.info(request, 'Вы подтвердили комент : ' + comment.content[:15])
	return redirect(reverse('adminka:comments_of_forecast', kwargs={'forecast_id': comment.forecast.id}))

def disapprove_comment_forecast(request, comment_id):
	comment = get_object_or_404(ForecastComment, pk=comment_id)
	comment.is_approved = False
	comment.save()
	messages.info(request, 'Вы скрыли комент : ' + comment.content[:15])
	return redirect(reverse('adminka:comments_of_forecast', kwargs={'forecast_id': comment.forecast.id}))

def delete_comment_forecast(request, comment_id):
	comment = get_object_or_404(ForecastComment, pk=comment_id)
	content = comment.content
	forecast_id = comment.forecast.id
	comment.delete()
	messages.info(request, 'Вы удалили комент : ' + content[:15])
	return redirect(reverse('adminka:comments_of_forecast', kwargs={'forecast_id': forecast_id}))

def mediafiles(request):
	args = {}
	args['files'] = MediaFile.objects.all()
	template = 'adminka/mediafiles.html'
	return render(request, template, args)

def delete_mediafile(request, file_id):
	file = get_object_or_404(MediaFile, id=file_id)
	title = file.description
	file.delete()
	messages.info(request, 'Вы удалили медиафайл ' + title)
	return redirect(reverse('adminka:mediafiles'))

def create_mediafile(request):
	args = {}
	args.update(csrf(request))
	form = MediaFileForm()

	if request.POST:
		form = MediaFileForm(request.POST, request.FILES)
		if form.is_valid() :
			file = form.save()
			title = file.description
			messages.info(request, 'Медиафайл ' + title + ' успешно создан. ')
			return redirect(reverse('adminka:mediafiles'))
	args['form'] = form
	template = 'adminka/create_mediafile.html'
	return render(request, template, args)

def edit_mediafile(request, file_id):
	args = {}
	args.update(csrf(request))
	instance = get_object_or_404(MediaFile, id=file_id)
	if request.method == 'POST':
		form = MediaFileForm(request.POST, request.FILES, instance=instance)
		if form.is_valid() :
			file = form.save()
			title = file.description
			messages.info(request, 'Медиа Файл ' + title + ' успешно изменен. ')
			return redirect(reverse('adminka:mediafiles'))
	else:
		form = MediaFileForm(instance=instance)
	args['form'] = form
	template = 'adminka/create_mediafile.html'
	return render(request, template, args)