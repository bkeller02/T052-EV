from django import forms
from django.forms import ModelForm
from .models import ContactSupport
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField


class NewAdminForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

	def save(self, commit=True):
		user = super(NewAdminForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class ContactForm(forms.Form):
	full_name = forms.CharField(max_length=100)
	email = forms.EmailField(required=True, max_length=150)
	phone_number = PhoneNumberField()
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea, max_length=2000)
	file_upload = forms.FileField(required=False)

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['phone_number'].help_text = "Enter a valid phone number (e.g. +12125552368)."

class ContactSupportForm(ModelForm):
	class Meta:
		model = ContactSupport
		fields = ["username", "email", "subject", "message", "file_upload"]
