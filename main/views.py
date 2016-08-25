from django.shortcuts import render
from custom_code.decorators import email_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from promis.models import Promis

def main(request):
	# Инициализация переменных
	args = {}
	args['promises'] = Promis.objects.filter(is_approved=True)[:10]
	template = 'main/main.html'
	return render(request, template, args)

@login_required(login_url=reverse_lazy('auths:signin'))
@email_required
def test(request):
	# Инициализация переменных
	args = {}
	messages.info(request, 'Чтобы совершить данное действие вам нужно авторизоваться. ')
	template = 'main/main.html'
	return render(request, template, args)

