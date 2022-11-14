from django.db import models
from django.urls import reverse


class Joke(models.Model):
    title = models.CharField('Название',max_length=255)
    content = models.TextField('Описание')
    author = models.ForeignKey('Creator', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_id': self.pk})

class Addition(models.Model):
    content = models.TextField('Текст добивки')
    joke_id = models.ForeignKey('Joke', on_delete=models.PROTECT, null=False)

class Creator(models.Model):
    login = models.CharField(max_length=255)

    def __str__(self):
        return self.login
