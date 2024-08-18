# app/forms.py
from django import forms
from ..models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        
    def __init__(self,*args, **kwargs):
        super(ContactForm,self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['name'].widget.attrs['class'] = 'form-control'    
        
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['class'] = 'form-control'    
        
        self.fields['message'].widget.attrs['placeholder'] = 'Message'
        self.fields['message'].widget.attrs['class'] = 'form-control'    