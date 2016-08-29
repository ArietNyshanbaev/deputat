# Импорт пакетов Python
from datetime import datetime
# Импорт стандартных пакетов Django
from django.db import models
from django.contrib.auth.models import User
from person.models import Person
# Импорт Моделей из Баззы данных

class News(models.Model):
	""" Класс для хранения Обещаний """
	title = models.CharField('Заголовок', max_length=200, null=True, blank=True)
	body = models.TextField('Тело' )
	date = models.DateTimeField('Дата', null=True, blank=True, auto_now_add=True )
	photo = models.ImageField('Фото', upload_to='media/news', null=True, blank=True)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = "New"
		verbose_name_plural = "News"


class NewsComment(models.Model):
	""" Класс для хранения Коментариев Обещаний """

	user = models.ForeignKey(User, verbose_name='Пользователь')
	news = models.ForeignKey(News, verbose_name='Принадлежит к новости')
	comment = models.ForeignKey('self', null=True, blank=True)
	date = models.DateTimeField(default=datetime.now)
	content = models.TextField('Контент')
	is_approved = models.BooleanField('Потвержден?', default=False)

	def __unicode__(self):
		return str(self.content)

	class Meta:
		verbose_name = "Коментарий"
		verbose_name_plural = "Коментарии"