from django import forms
class ticketFrom(forms.Form):
    ticket_id = forms.CharField(max_length=30)
    title = forms.CharField(max_length=60)
    resolved = forms.IntegerField()
    read = forms.IntegerField()
    description = forms.CharField(max_length=256)
    user = forms.CharField(max_length=60)
