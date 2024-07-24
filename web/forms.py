from django import forms
from .models import ContactForm

class Contact_Form(forms.Form):
    customer_name = forms.CharField(max_length=64, label='Nombre')
    customer_email = forms.EmailField(label='Correo')
    message = forms.CharField(label='Mensaje')

class Contactillo(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_name', 'customer_email', 'message']
    







