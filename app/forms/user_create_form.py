from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserCreateForm(UserCreationForm):

    class Meta:
        # fields = ('_all_')
        fields = ('first_name','last_name','username','email','password1','password2')
        model = User

    def __init__(self,*args, **kwargs):
        super(UserCreateForm,self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        
    
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        
        self.fields['username'].widget.attrs['placeholder'] = ' Username'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        # self.fields['mobile_no'].widget.attrs['placeholder'] = 'Mobile No'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
        # self.fields['phone'].widget.attrs['placeholder'] = 'Mobile No'