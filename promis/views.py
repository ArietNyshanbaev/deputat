from django.shortcuts import render, redirect, get_object_or_404
from custom_code.decorators import email_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from .models import Promis, Result, PromisRank, Comments
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse 

@login_required(login_url=reverse_lazy('auths:signin'))
@email_required
def add_promis(request, key='main'):
	# initialize variables
	args={}
	args.update(csrf(request))

	if request.POST:
		link = request.POST.get('link', '')
		body = request.POST.get('content', '')
		promis = Promis.objects.create(link=link, body=body, user=request.user)
	messages.info(request, 'Спасибо обещание отправлено модератору на просмотр.')
	return redirect(reverse('main:main'))

def detailed_promis(request, promis_id):
	# initialize variables
	args={}
	promis = get_object_or_404(Promis, pk=promis_id)
	args['comments'] = Comments.objects.filter(promis=promis, comment=None, is_approved=True)
	args['comments_all'] = Comments.objects.filter(promis=promis, is_approved=True)
	args['promis'] = promis
	args['positive_rank'] = PromisRank.objects.filter(promis=promis, positive=True).count()
	args['negative_rank'] = PromisRank.objects.filter(promis=promis, positive=False).count()
	if PromisRank.objects.filter(promis=promis).count() > 0:
		args['rank_persentage'] = PromisRank.objects.filter(promis=promis, positive=True).count() / PromisRank.objects.filter(promis=promis).count() * 100
		print PromisRank.objects.filter(promis=promis, positive=True).count() / PromisRank.objects.filter(promis=promis).count() * 100
	return render(request, 'promis/detailed_promis.html', args)

def new_promises(request):
	# initialize variables
	args={}
	args['promises'] = Promis.objects.filter(is_approved=True, status='Новое')
	return render(request, 'promis/new_promises.html', args)

def done_promises(request):
	# initialize variables
	args={}
	args['promises'] = Promis.objects.filter(is_approved=True, status='Выполнено')
	return render(request, 'promis/done_promises.html', args)

def not_done_promises(request):
	# initialize variables
	args={}
	args['promises'] = Promis.objects.filter(is_approved=True, status='Не выполнено')
	return render(request, 'promis/not_done_promises.html', args)

@login_required(login_url=reverse_lazy('auths:signin'))
@email_required
def add_result(request):
	# initialize variables
	args={}
	args.update(csrf(request))

	if request.POST:
		content = request.POST.get('content', '')
		promis_id = request.POST.get('promis_id', '')
		promis = get_object_or_404(Promis, pk=promis_id)
		result = Result.objects.create(text=content, user=request.user, promis=promis)
	messages.info(request, 'Спасибо ваш итог отправлено модератору на просмотр.')
	return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url=reverse_lazy('auths:signin'))
@email_required 
def believe(request, promis_id):
	# initialize variables
	args={}
	promis = get_object_or_404(Promis, pk=promis_id)

	if PromisRank.objects.filter(user=request.user, promis=promis).exists():
		rank = PromisRank.objects.filter(user=request.user, promis=promis)[0]
		rank.positive = True;
		rank.save()
	else:
		rank = PromisRank.objects.create(user=request.user, positive=True, promis=promis)
	messages.info(request, 'Спасибо, ваш голос учтен.')
	return redirect(reverse('promis:detailed_promis', kwargs={'promis_id':promis.id}))

def not_believe(request, promis_id):
	# initialize variables
	args={}
	promis = get_object_or_404(Promis, pk=promis_id)

	if PromisRank.objects.filter(user=request.user, promis=promis).exists():
		rank = PromisRank.objects.filter(user=request.user, promis=promis)[0]
		rank.positive = False;
		rank.save()
	else:
		rank = PromisRank.objects.create(user=request.user, positive=False, promis=promis)
	messages.info(request, 'Спасибо, ваш голос учтен.')
	return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url=reverse_lazy('auths:signin'))
@email_required 
def add_comment(request, promis_id, comment_id=None):
	promis = get_object_or_404(Promis, id=promis_id)
	content = request.POST.get('content', '')
	new_comment = Comments.objects.create(user=request.user,promis=promis, content=content )
	if comment_id:
		comment = get_object_or_404(Comments, id=comment_id)
		new_comment.comment = comment
		new_comment.save()
	messages.info(request, 'Ваш комментарий будет отображаться как только пройдет модерацию.')
	return redirect(reverse('promis:detailed_promis', kwargs={'promis_id':promis.id}))

