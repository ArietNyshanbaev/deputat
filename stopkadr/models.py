from django.db import models
import os
# third party packages imports
from PIL import Image, ImageOps
# python packages imports
import StringIO
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.core.files.uploadedfile import InMemoryUploadedFile
# Импорт Моделей из Баззы данных

class MediaFile(models.Model):
	""" Класс для хранения Обещаний """
	description = models.CharField('Описание', max_length=1000, null=True, blank=True)
	date = models.DateTimeField('Дата', null=True, blank=True, auto_now_add=True )
	photo = models.ImageField('Фото', upload_to='media/photo', null=True, blank=True)
	video = models.FileField('Видео', upload_to='media/video', null=True, blank=True)
	is_video = models.BooleanField('Видео?', default=False)


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
		super(MediaFile, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.description

	class Meta:
		verbose_name = "Медиа Файл"
		verbose_name_plural = "Медиа Файлы"