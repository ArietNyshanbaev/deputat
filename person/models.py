# Импорт пакетов Python
from datetime import datetime
# Импорт стандартных пакетов Django
from django.db import models
from django.contrib.auth.models import User
# Импорт Моделей из Баззы данных

MARITAL_STATUS_LIST = (
		(u'Женат / Замужем', 'Женат / Замужем'),
		(u'Разведен / Разведена', 'Разведен / Разведена'),
		(u'Вдова / Вдовец', 'Вдова / Вдовец'),
		(u'Холостой / Не замужем', 'Холостой / Не замужем '),
	)

class Province(models.Model):
	""" Класс для хранения Областей """
	title = models.CharField('Область ', max_length=100)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = "Область"
		verbose_name_plural = "Область"

class Region(models.Model):
	""" Класс для хранения Районов """
	title = models.CharField('Район', max_length=100)
	province = models.ForeignKey(Province, verbose_name='Область')
	is_city = models.BooleanField('Город?')

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = "Район"
		verbose_name_plural = "Районы"

class Category(models.Model):
	""" Класс который определяет категорию депутата """
	title = models.CharField('Название', max_length=100)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"

class Party(models.Model):
	""" Класс который определяет партию депутата """
	title = models.CharField('Партия', max_length=100)
	logo = models.ImageField('Лого', upload_to='media', null=True, blank=True)
	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = "Партия"
		verbose_name_plural = "Партии"

class Person(models.Model):
	""" Класс Таблица Человек как субъект """

	last_name = models.CharField('Фамилия субъекта', max_length=100)
	first_name = models.CharField('Имя субъекта', max_length=100)
	middle_name = models.CharField('Отчество субъекта', max_length=100)
	marital_status = models.CharField('Нике(Семейное положение субъекта)', max_length=100, choices=MARITAL_STATUS_LIST,)
	biography = models.TextField()
	contacts = models.CharField('Контактные данные', max_length=100, null=True, blank=True)
	estate = models.TextField(null=True, blank=True)
	category = models.ForeignKey(Category, verbose_name='Категория')
	region = models.ForeignKey(Region, verbose_name='Районы', null=True, blank=True)
	party = models.ForeignKey(Party, verbose_name='Партия')
	photo = models.ImageField('фото', upload_to='media', null=True, blank=True)

	def __unicode__(self):
		return self.first_name + " " + self.last_name

	class Meta:
		verbose_name = "Персона"
		verbose_name_plural = "Персоны"

class Karma(models.Model):
	""" Karma class for particular user """
	person = models.ForeignKey(Person, verbose_name='Принадлежит к Персоне')
	positive = models.BooleanField('Позитивный?', default=True)
	user = models.ForeignKey(User, verbose_name='Принадлежит пользователю') 

	def __unicode__(self):
		return str(self.user.username) + ' ' + str(self.person)

	class Meta:
		verbose_name = "Карма"
		verbose_name_plural = "Кармы"