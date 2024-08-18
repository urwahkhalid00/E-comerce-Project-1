from django import forms
from ..models import Order


class CheckoutForm(forms.ModelForm):
    first_name = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : 'First Name', 'class' : 'form-control' } ) )
    last_name = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : 'last Name', 'class' : 'form-control' } ) )
    email = forms.EmailField( widget= forms.TextInput( attrs={'placeholder' : 'Email' , 'class' : 'form-control'} ) )
    phone = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : 'Phone', 'class' : 'form-control' } ) )
    address = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : ' Enter address' , 'class' : 'form-control'} ) )
    country = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : ' Country ' , 'class' : 'form-control'} ) )
    city = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : ' City ', 'class' : 'form-control' } ) )
    state = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : ' State ' , 'class' : 'form-control'} ) )
    zip_code = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : ' Zip / Postal Code ', 'class' : 'form-control' } ) )
    note = forms.Textarea( )
    user = forms.CharField(required=False)

    class Meta:

        fields = ('__all__')
        model = Order
        