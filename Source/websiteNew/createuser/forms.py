from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100, widget=forms.TextInput, required=true)
    password = forms.CharField(label="Password", max_length=20, widget=forms.PasswordInput, required=true)
    email = forms.CharField(label="Email", max_length=50, widget=forms.EmailInput, required=true)
    phoneNumber = forms.CharField(label="Phone number", max_length=20, widget=forms.NumberInput, required=true)

