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
        fields = ['content', 'joke_id']
        widgets = {
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите начало шутки'
            }),
        }

