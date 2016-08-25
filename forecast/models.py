# Импорт пакетов Python
from datetime import datetime
# Импорт стандартных пакетов Django
from django.db import models
from django.contrib.auth.models import User
from person.models import Person
# Импорт Моделей из Баззы данных

class Forecast(models.Model):
	""" Класс для хранения Мнениe """
	person = models.ForeignKey(Person, verbose_name='Депутат')
	title = models.CharField('Заголoвoк', max_length=200)
	body = models.TextField('Тело')
	date = models.DateTimeField('Дата' )
	user = models.ForeignKey(User, verbose_name='Эксперт')
	is_approved = models.BooleanField('Потвержден?', default=False)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = "Мнение"
		verbose_name_plural = "Мнения"

class ForecastRank(models.Model):
	""" Класс для хранения Рейтинга Mнений """
	forecast = models.ForeignKey(Forecast, verbose_name='Принадлежит к Мнению')
	positive = models.BooleanField('Позитивный?', default=True)
	user = models.ForeignKey(User, verbose_name='Принадлежит пользователю') 

	def __unicode__(self):
		return str(self.positive)

	class Meta:
		verbose_name = "Рейтинг Mнения"
		verbose_name_plural = "Рейтинг Mнений"