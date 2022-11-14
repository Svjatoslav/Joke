from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, HiddenInput
from .models import Joke, Addition


class JokesForm(ModelForm):
    class Meta:
        model = Joke
        fields = ['title', 'content']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите начало шутки'
            }),
        }


class AdditionsForm(ModelForm):
    # def __init__(self, **kwargs):
    #     self.joke_id = kwargs.pop('joke_id', None)
    #     super(AdditionsForm, self).__init__(**kwargs)
    #
    # def save(self,commit=True):
    #     obj = super(AdditionsForm,self).save(commit=False)
    #     obj.joke_id=self.joke_id
    #     if commit:
    #         obj.save()
    #     return obj

    class Meta:
        model = Addition
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите начало шутки'
            }),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
