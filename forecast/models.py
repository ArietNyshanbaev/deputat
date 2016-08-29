# Импорт пакетов Python
from datetime import datetime
# Импорт стандартных пакетов Django
from django.db import models
from django.contrib.auth.models import User
from person.models import Person
# Импорт Моделей из Баззы данных

class Forecast(models.Model):
	""" Класс для хранения Мнениe """
	expert = models.CharField('Эксперт ', max_length=200)
	title = models.CharField('Заголoвoк ', max_length=200)
	body = models.TextField('Тело')
	date = models.DateField('Дата')
	user = models.ForeignKey(User, verbose_name='Добавлено пользователем')
	is_approved = models.BooleanField('Потвержден?', default=True)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = "Мнение"
		verbose_name_plural = "Мнения"

class ForecastComment(models.Model):
	""" Класс для хранения Коментариев Мнений """

	user = models.ForeignKey(User, verbose_name='Пользователь')
	forecast = models.ForeignKey(Forecast, verbose_name='Принадлежит к мнению')
	comment = models.ForeignKey('self', null=True, blank=True)
	date = models.DateTimeField(default=datetime.now)
	content = models.TextField('Контент')
	is_approved = models.BooleanField('Потвержден?', default=False)

	def __unicode__(self):
		return str(self.content)

	class Meta:
		verbose_name = "Коментарий"
		verbose_name_plural = "Коментарии"