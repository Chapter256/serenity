from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('fname', 'sname', 'email', 'subject', 'body',)

        labels = {
            'fname': 'First Name',
            'sname': 'Surname',
            'email': 'Email',
            'subject': 'Subject',
            'body': 'Message',
        }