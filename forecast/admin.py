# Импорт стандартных пакетов Django
from django.contrib import admin
# Импорт моделей из баззы данных
from .models import Forecast, ForecastRank

class ForecastAdmin(admin.ModelAdmin):
	""" Класс Регистрации Админки для Клеинтов """
	list_display = ('person', 'title', 'is_approved')
	list_filter = ('is_approved','date')
admin.site.register(Forecast, ForecastAdmin)

class ForecastRankAdmin(admin.ModelAdmin):
	""" Класс Регистрации Админки для Движимости """
	list_display = ('forecast', 'positive', 'user')
	list_filter = ('user','positive')
admin.site.register(ForecastRank, ForecastRankAdmin)