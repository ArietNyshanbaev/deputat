# Импорт пакетов Python
from datetime import datetime
# Импорт стандартных пакетов Django
from django.db import models
from django.contrib.auth.models import User
from person.models import Person
# Импорт Моделей из Баззы данных

STATUS_LIST = (
		(u'Новое ', 'Новое'),
		(u'Выполнено', 'Выполнено'),
		(u'Не выполнено', 'Не выполненом'),
	)
class Promis(models.Model):
	""" Класс для хранения Обещаний """
	user = models.ForeignKey(User, verbose_name=' Добавлено пользователем ')
	person = models.ForeignKey(Person, verbose_name='Депутат', null=True, blank=True)
	title = models.CharField('Заголовок', max_length=200, default='Еще не задан')
	body = models.TextField('Тело' )
	date = models.DateField('Дата обещания', null=True, blank=True )
	deadline = models.DateField('Последний срок', null=True, blank=True)
	is_approved = models.BooleanField('Потвержден?', default=False)
	link = models.CharField(' Источник ', max_length=500)
	screenshot = models.ImageField('Скриншот', upload_to='media/link_screen', null=True, blank=True)
	status = models.CharField('Статус обещания', default='Новое', max_length=50, choices=STATUS_LIST)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = "Обещание"
		verbose_name_plural = "Обещания"

class PromisRank(models.Model):
	""" Класс для хранения Рейтинга Обещаний """
	promis = models.ForeignKey(Promis, verbose_name='Принадлежит к Обещанию')
	positive = models.BooleanField('Позитивный?', default=True)
	user = models.ForeignKey(User, verbose_name='Принадлежит пользователю') 

	def __unicode__(self):
		return str(self.promis)

	class Meta:
		verbose_name = "Рейтинг Mнения"
		verbose_name_plural = "Рейтинг Mнений"

class Result(models.Model):
	""" Класс для хранения Результатов Обещаний """

	text = models.TextField('Контент')
	promis = models.ForeignKey(Promis, verbose_name='Принадлежит к Обещанию')
	user = models.ForeignKey(User, verbose_name='Принадлежит пользователю') 

	def __unicode__(self):
		return str(self.promis)

	class Meta:
		verbose_name = "Результат"
		verbose_name_plural = "Результаты"

class Comments(models.Model):
	""" Класс для хранения Коментариев Обещаний """

	user = models.ForeignKey(User, verbose_name='Пользователь')
	promis = models.ForeignKey(Promis, verbose_name='Принадлежит к Обещанию')
	comment = models.ForeignKey('self', null=True, blank=True)
	date = models.DateTimeField(default=datetime.now())
	content = models.TextField('Контент')
	is_approved = models.BooleanField('Потвержден?', default=False)

	def __unicode__(self):
		return str(self.content)

	class Meta:
		verbose_name = "Коментарий"
		verbose_name_plural = "Коментарии"


