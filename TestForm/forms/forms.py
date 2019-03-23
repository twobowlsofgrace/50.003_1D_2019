from django import forms

class BasicForm(forms.Form):
	title = forms.CharField(label="Title", max_length=150, widget=forms.TextInput, required=True)
	description = forms.CharField(label="Description", max_length=300, widget=forms.TextInput, required=True)
	name = forms.CharField(label="Name", max_length=20, widget=forms.TextInput, required=True)
	phonenumber = forms.CharField(label="Phonenumber", max_length=20, widget=forms.TextInput, required=True)
	email = forms.CharField(label="Email", max_length=50, widget=forms.EmailInput, required=True)
