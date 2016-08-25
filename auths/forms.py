from django import forms
from django.core.validators import validate_email
# validation of user
from django.forms.utils import ErrorList
from django.contrib.auth.models import User
from .models import Verification

class SigninForm(forms.Form):
	username = forms.CharField(
		label=' Логин ', 
		required=True, 
		max_length=100,
		widget=forms.TextInput(attrs={'required': 'true'})
	)
	password = forms.CharField(
		label=' Пароль ',
		required=True, 
		widget=forms.PasswordInput(attrs={'required': 'true'})
	)

class SignupForm(forms.Form):
	""" Форма для регистрации пользователей """
	username = forms.CharField(
		label=' Логин ', 
		required=True, 
		max_length=100,
		widget=forms.TextInput(attrs={'required': 'true'})
	)

	email = forms.CharField(
		label=' Email',
		required=True,
		max_length=100,
		widget=forms.EmailInput(attrs={'required': 'true'})
	)

	password = forms.CharField(
		label=' Пароль ',
		required=True, 
		widget=forms.PasswordInput(attrs={'required': 'true'})
	)

	def clean_email(self):
		cd = self.cleaned_data
		try:
			validate_email(cd['email'])
		except forms.ValidationError:
			raise forms.ValidationError('Введите Еmail в правильной форме')
		if User.objects.filter(username=cd['email']).exists():
			raise forms.ValidationError('Этот email уже используется')
		return cd['email']

class ChangePasswordForm(forms.Form):
	current_password = forms.CharField(
		label=' Нынешний пароль ',
		required=True, 
		widget=forms.PasswordInput(attrs={'required': 'true'})
	)
	new_password = forms.CharField(
		label=' Новый пароль ',
		required=True, 
		widget=forms.PasswordInput(attrs={'required': 'true'})
	)
	repeate_new_password = forms.CharField(
		label=' Повторите новый пароль ',
		required=True, 
		widget=forms.PasswordInput(attrs={'required': 'true'})
	)

	def clean_repeate_new_password(self):
		cd = self.cleaned_data
		if cd['repeate_new_password'] != cd['new_password'] :
			raise forms.ValidationError('Новые пароли не совпадают.')
		return cd['repeate_new_password']
