# python packages imports
from datetime import datetime 
# django core packeges imports
from django.db import models
from django.contrib.auth.models import User

class Verification(models.Model):
	""" Class to verify user's email """

	is_verified = models.BooleanField('подтвержден ?', default=False)
	user = models.OneToOneField(User, primary_key=True, verbose_name='ползователь')
	random_string = models.CharField('random_string', max_length=32)

	class Meta:
		verbose_name = "Подтверждение Email(a)"
		verbose_name_plural = "Подтверждение Email(ов)"

	def __unicode__(self):
		return str(self.user.username)

class Domain(models.Model):
	""" Domain name class """
	domain = models.CharField('Ваш домен', max_length=100)

	class Meta:
		verbose_name = "Доменное имя"
		verbose_name_plural = "Доменное имя"

	def __unicode__(self):
		return self.domain
