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
	date = models.DateTimeField('Дата', null=True, blank=True )
	photo = models.ImageField('Фото', upload_to='media/news', null=True, blank=True)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = "New"
		verbose_name_plural = "News"