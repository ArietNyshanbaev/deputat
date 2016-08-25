# Импорт стандартных пакетов Django
from django.contrib import admin
# Импорт моделей из баззы данных
from .models import Person , Region, Karma, Province, Category, Party

class PersonAdmin(admin.ModelAdmin):
	""" Класс Регистрации Админки для Клеинтов """
	list_display = ('first_name', 'last_name', 'category')
	list_filter = ('category',)
admin.site.register(Person, PersonAdmin)

admin.site.register(Province)

class RegionAdmin(admin.ModelAdmin):
	""" Класс Регистрации Админки для Движимости """
	list_display = ('title', 'province', 'is_city')
	list_filter = ('province','is_city')
admin.site.register(Region, RegionAdmin)

admin.site.register(Category)
admin.site.register(Party)

class KarmaAdmin(admin.ModelAdmin):
	""" Класс Регистрации Админки для Нотариального документа """
	list_display = ('person','user', 'positive')
	list_filter = ('positive','user', 'person')
admin.site.register(Karma, KarmaAdmin)
