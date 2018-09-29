from django import forms

from .models import Person

class PostForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('first_name', 'last_name', 'phone_number', 'email_address', 'street_address')