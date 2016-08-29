from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse 
from custom_code.decorators import email_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from .models import News, NewsComment

def main(request):
	# Инициализация переменных
	args = {}
	args['news'] = News.objects.all()
	template = 'news/main.html'
	return render(request, template, args)

def detailed_news(request, news_id):
	# Инициализация переменных
	args = {}
	news = get_object_or_404(News, pk=news_id)
	args['comments'] = NewsComment.objects.filter(news=news, comment=None, is_approved=True)
	args['comments_all'] = NewsComment.objects.filter(news=news, is_approved=True)
	args['new'] = news
	args['other_news'] = News.objects.all().exclude(pk=news.id).order_by('-id')[:10]
	template = 'news/detailed_news.html'
	return render(request, template, args)

@login_required(login_url=reverse_lazy('auths:signin'))
@email_required 
def add_comment(request, news_id, comment_id=None):
	news = get_object_or_404(News, id=news_id)
	content = request.POST.get('content', '')
	new_comment = NewsComment.objects.create(user=request.user,news=news, content=content )
	if comment_id:
		comment = get_object_or_404(NewsComment, id=comment_id)
		new_comment.comment = comment
		new_comment.save()
	messages.info(request, 'Ваш комментарий будет отображаться как только пройдет модерацию.')
	return redirect(reverse('news:detailed_news', kwargs={'news_id':news.id}))
