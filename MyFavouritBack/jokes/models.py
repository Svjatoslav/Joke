from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Joke(models.Model):
    title = models.CharField('Название',max_length=255)
    content = models.TextField('Описание')
    creator = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Автор')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_id': self.pk})

class Addition(models.Model):
    content = models.TextField('Текст добивки')
    joke_id = models.ForeignKey('Joke', on_delete=models.PROTECT, null=False)
