from django import forms
from todolist_functions_views.models import SimpleUser
class UserForm(forms.ModelForm):
    name = forms.CharField(label='nom', max_length=30,required=True, error_messages={
               'required': 'Veuillez entrer votre nom'
                })
    password = forms.CharField(label="mot de passe", max_length=32,required=True,min_length=8,error_messages={
               'required': 'Veuillez entrer un mot de passe',
               'min_length':"Le mot de passe doit est court"
                })
    
    class Meta:
        model = SimpleUser
        fields = ['name','password']