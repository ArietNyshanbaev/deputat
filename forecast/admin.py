# Импорт стандартных пакетов Django
from django.contrib import admin
# Импорт моделей из баззы данных
from .models import Forecast, ForecastComment

class ForecastAdmin(admin.ModelAdmin):
	""" Класс Регистрации Админки для Клеинтов """
	list_display = ('expert', 'title', 'is_approved')
	list_filter = ('is_approved','date')
admin.site.register(Forecast, ForecastAdmin)
admin.site.register(ForecastComment)