from django import forms
# validation of user
from django.forms.utils import ErrorList
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
from person.models import Person, MARITAL_STATUS_LIST, Category, Party, Region


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