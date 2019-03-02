from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100, widget=forms.TextInput)
    password = forms.CharField(label="Password", max_length=20, widget=forms.PasswordInput)
    id = forms.CharField(label="ID", max_length=50, widget=forms.NumberInput)
    email = forms.CharField(label="Email", max_length=50, widget=forms.EmailInput)
    phoneNumber = forms.CharField(label="Phone number", max_length=20, widget=forms.NumberInput)

