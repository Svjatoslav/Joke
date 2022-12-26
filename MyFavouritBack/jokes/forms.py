from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, HiddenInput, NumberInput
from .models import Joke, Addition, Rating, Profile


class JokesForm(ModelForm):
    # добавление данных в модель
    class Meta:
        model = Joke
        fields = ['content']
        widgets = {
                'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите начало шутки',
                'size': 2,
            }),
        }


class AdditionsForm(ModelForm):
    class Meta:
        model = Addition
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Добей шутку',
                'rows': 2,
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


class RatingForm(ModelForm):

    class Meta:
        model = Rating
        fields = ['rating']
        widgets = {
            'rating': NumberInput(attrs={
                'class': 'form-control',
            }),
        }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic')
        widgets = {
            'bio': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите о себе пару слов',
                'rows': 3})
        }