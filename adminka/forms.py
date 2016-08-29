from django import forms
# validation of user
from django.forms.utils import ErrorList
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
from person.models import Person, MARITAL_STATUS_LIST, Category, Party, Region
from news.models import News
from forecast.models import Forecast
from promis.models import Promis, STATUS_LIST


class PersonForm(forms.ModelForm):
	first_name =  forms.CharField(
		label=' Имя ', 
		required=True, 
		max_length=100,
		widget=forms.TextInput(attrs={'required': 'true', 'class':'form-control'})
	)

	last_name =  forms.CharField(
        label=' Фамилия  ', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(attrs={'required': 'true', 'class':'form-control'})
	)

	middle_name =  forms.CharField(
        label=' Отчество ', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(attrs={'required': 'true', 'class':'form-control'})
    )

	marital_status = forms.ChoiceField(label=' Семейное положение ', choices=MARITAL_STATUS_LIST, widget=forms.Select(attrs={'class':'form-control'}))

	biography = forms.CharField(label=' Биография ', widget=CKEditorWidget(config_name='awesome_ckeditor'))

	contacts = forms.CharField(
		label=' Контактные данные ', 
		required=True, 
		max_length=100,
		widget=forms.TextInput(attrs={'required': 'true', 'class':'form-control'})
	)

	estate = forms.CharField(label=' Имушество ', widget=CKEditorWidget(config_name='awesome_ckeditor'))

	category = forms.ModelChoiceField(label=' Кенеш ', queryset=Category.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))

	region = forms.ModelChoiceField(label=' Регион ', queryset=Region.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))

	party = forms.ModelChoiceField(label=' Партия ', queryset=Party.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))

	class Meta:
		model = Person
		exclude = ()

class NewsForm(forms.ModelForm):
	title = forms.CharField(
		label=' Заголовок ', 
		required=True, 
		max_length=200,
		widget=forms.TextInput(attrs={'required': 'true', 'class':'form-control'})
	)

	body = forms.CharField(label=' Тело ', widget=CKEditorWidget(config_name='awesome_ckeditor'))

	class Meta:
		model = News
		exclude = ('date',)

class PromisForm(forms.ModelForm):
	title = forms.CharField(
		label=' Заголовок ', 
		required=True, 
		max_length=200,
		widget=forms.TextInput(attrs={'required': 'true', 'class':'form-control'})
	)

	person = forms.ModelChoiceField(label=' Депутат ', queryset=Person.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))

	body = forms.CharField(label=' Тело ', widget=CKEditorWidget(config_name='awesome_ckeditor'))

	date = forms.DateField(label=' Дата обещания ', widget=forms.TextInput(attrs={'type':'date', 'class':'form-control'}))

	deadline = forms.DateField(label=' Последний день ', widget=forms.TextInput(attrs={'type':'date', 'class':'form-control'}))

	is_approved  = forms.BooleanField(label=' Потверждение ', widget=forms.CheckboxInput(attrs={'class':'form-control'}))

	link = forms.CharField(
		label=' Источник ', 
		required=True, 
		max_length=200,
		widget=forms.TextInput(attrs={'required': 'true', 'class':'form-control'})
	)

	status = forms.ChoiceField(label=' Статус обещания ', choices=STATUS_LIST, widget=forms.Select(attrs={'class':'form-control'}))

	class Meta:
		model = Promis
		exclude = ('user',)

class ForecastForm(forms.ModelForm):
	
	title = forms.CharField(
		label=' Заголовок ', 
		required=True, 
		max_length=200,
		widget=forms.TextInput(attrs={'required': 'true', 'class':'form-control'})
	)

	date = forms.DateField(label=' Дата ', widget=forms.TextInput(attrs={'type':'date', 'class':'form-control'}))

	expert = forms.CharField(
		label=' Эксперт ', 
		required=True, 
		max_length=200,
		widget=forms.TextInput(attrs={'required': 'true', 'class':'form-control'})
	)

	body = forms.CharField(label=' Тело ', widget=CKEditorWidget(config_name='awesome_ckeditor'))


	class Meta:
		model = Forecast
		exclude = ('user','is_approved',)

