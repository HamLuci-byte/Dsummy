from django import forms
from.models import Blog

class Form(forms.Form):
	text = forms.CharField()
	info = forms.IntegerField()

class Formm(forms.Form):
	text = forms.CharField()

class URLForm(forms.Form):
	url = forms.URLField()

class DataForm(forms.Form):
	data = forms.CharField()

class ContactForm(forms.Form):
	fname = forms.CharField(widget = forms.TextInput(
		attrs={
			'class':'form-control',
		}
	))
	lname = forms.CharField(widget = forms.TextInput(
		attrs={
			'class':'form-control',
		}
	))
	email = forms.EmailField(widget = forms.TextInput(
		attrs={
			'class':'form-control',
		}
	))
	subject = forms.CharField(widget = forms.TextInput(
		attrs={
			'class':'form-control',
		}
	))
	message = forms.CharField(widget = forms.Textarea(
		attrs={
			'class':'form-control',
			'cols':'30',
			'rows':'7',
		}
	))

	





	