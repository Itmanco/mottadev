from django import forms
from . models import Contact


class CreateContactForm(forms.ModelForm):

    class Meta:
        model = Contact

        fields = ['name', 'email', 'textMessage', 'phone', 'location']
        exclude = ['creation_date']

    def __init__(self, *args, **kwargs):
        super(CreateContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['email'].label = ""
        self.fields['textMessage'].label = ""
        self.fields['phone'].label = ""
        self.fields['location'].label = ""

        self.fields['name'].widget.attrs['placeholder'] = "your name (required)"
        self.fields['email'].widget.attrs['placeholder'] = "Your email (required)"
        self.fields['textMessage'].widget.attrs['placeholder'] = "How can we help? (required)"
        self.fields['phone'].widget.attrs['placeholder'] = "Your phone number (required)"
        self.fields['location'].widget.attrs['placeholder'] = "Location (required)"


