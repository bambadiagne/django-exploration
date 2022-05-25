from django import forms
from . import status_task
from todolist_functions_views.models import SimpleUser, Todo


class UserForm(forms.ModelForm):
    name = forms.CharField(label='nom', max_length=30, required=True, error_messages={
        'required': 'Veuillez entrer votre nom'
    })
    password = forms.CharField(label="mot de passe", max_length=32, required=True, min_length=8, error_messages={
        'required': 'Veuillez entrer un mot de passe',
        'min_length': "Le mot de passe doit est court"
    })

    class Meta:
        model = SimpleUser

        fields = ['name', 'password']


class TodoForm(forms.ModelForm):
    status = forms.ChoiceField(label='status', choices=status_task.STATUS_TASK, required=True, error_messages={
        'required': 'Veuillez choisir un status',
        'invalid_choice': '%(value)s n\'est pas  disponible dans la liste des status',
    },)
    task = forms.CharField(label="task", max_length=32, required=True, min_length=8, error_messages={
        'required': 'Veuillez entrer une tâche',

    })

    class Meta:
        model = Todo

        fields = ['status', 'task']
