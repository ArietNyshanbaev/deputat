# Импорт стандартных пакетов Django
from django.contrib import admin
# Импорт моделей из баззы данных
from .models import Promis, PromisRank, Result

class PromisAdmin(admin.ModelAdmin):
	""" Класс Регистрации Админки для Клеинтов """
	list_display = ('title', 'person', 'date', 'is_approved')
	list_filter = ('date','is_approved')
admin.site.register(Promis, PromisAdmin)

class PromisRankAdmin(admin.ModelAdmin):
	""" Класс Регистрации Админки для Движимости """
	list_display = ('promis', 'user')
	list_filter = ('promis',)
admin.site.register(PromisRank, PromisRankAdmin)

admin.site.register(Result)