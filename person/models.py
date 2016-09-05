# Импорт пакетов Python
from datetime import datetime
# Импорт стандартных пакетов Django
from django.db import models
from django.contrib.auth.models import User
# third party packages imports
from PIL import Image, ImageOps
# python packages imports
import StringIO
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.core.files.uploadedfile import InMemoryUploadedFile
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

	def save(self, *args, **kwargs):
		if self.photo:
			try:
				img = Image.open(StringIO.StringIO(self.photo.read()))

				if img.mode != 'RGB':
					img = img.convert('RGB')
				img_width = self.photo.width
				img_height = self.photo.height
				while img_width > 1300 or img_height > 1300:
					img_width /= 1.5
					img_height /= 1.5


				img.thumbnail((img_width, img_height), Image.ANTIALIAS)
				if img_width>img_height:
					size = (int(img_width),int(img_width*1.0))
				else:
					size = (int(img_height*1.34),int(img_height))

				image = img
				background = Image.new('RGBA', size, (255, 255, 255, 0))
				background.paste(image,((size[0] - image.size[0]) / 2, (size[1] - image.size[1]) / 2))

				output = StringIO.StringIO()
				background.save(output, format='JPEG', quality=70)
				output.seek(0)
				self.photo.delete(False)
				self.photo = InMemoryUploadedFile(output, 'ImageField', "file.jpg", 'image/jpeg', output.len, None)
			except IOError:
				pass
		super(Person, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.last_name + " " + self.first_name + " " + self.middle_name

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