from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse 
from custom_code.decorators import email_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from .models import MediaFile

def main(request):
	# Инициализация переменных
	args = {}
	args['files'] = MediaFile.objects.all()
	template = 'stopkadr/main.html'
	return render(request, template, args)

def detailed_mediafile(request, file_id):
	# Инициализация переменных
	args = {}
	file = get_object_or_404(MediaFile, pk=file_id)
	args['file'] = file
	template = 'stopkadr/detailed_mediafile.html'
	return render(request, template, args)