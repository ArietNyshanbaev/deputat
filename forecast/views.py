from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse 
from custom_code.decorators import email_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from .models import Forecast, ForecastComment

def main(request):
	# Инициализация переменных
	args = {}
	args['forecasts'] = Forecast.objects.all()
	template = 'forecast/main.html'
	return render(request, template, args)

def detailed_forecast(request, forecast_id):
	# Инициализация переменных
	args = {}
	forecast = get_object_or_404(Forecast, pk=forecast_id)
	args['comments'] = ForecastComment.objects.filter(forecast=forecast, comment=None, is_approved=True)
	args['comments_all'] = ForecastComment.objects.filter(forecast=forecast, is_approved=True)
	args['forecast'] = forecast
	args['other_forecasts'] = Forecast.objects.all().exclude(pk=forecast.id).order_by('-id')[:10]
	template = 'forecast/detailed_forecast.html'
	return render(request, template, args)

@login_required(login_url=reverse_lazy('auths:signin'))
@email_required 
def add_comment(request, forecast_id, comment_id=None):
	forecast = get_object_or_404(Forecast, id=forecast_id)
	content = request.POST.get('content', '')
	new_comment = ForecastComment.objects.create(user=request.user,forecast=forecast, content=content )
	if comment_id:
		comment = get_object_or_404(ForecastComment, id=comment_id)
		new_comment.comment = comment
		new_comment.save()
	messages.info(request, 'Ваш комментарий будет отображаться как только пройдет модерацию.')
	return redirect(reverse('forecast:detailed_forecast', kwargs={'forecast_id':forecast.id}))
