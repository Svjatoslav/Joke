from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Joke(models.Model):
    title = models.CharField('Название',max_length=255)
    content = models.TextField('Описание')
    time_created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Автор')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_id': self.pk})

class Addition(models.Model):
    content = models.TextField('Текст добивки')
    joke_id = models.ForeignKey('Joke', on_delete=models.PROTECT, null=False)
    creator = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Автор', related_name='creator')
    rating = models.FloatField(default = 0)
    marked_by_users = models.ManyToManyField(User, related_name='marked', blank=True)


class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="static/images/profile/")
    rating = models.FloatField(default = 0)
    # marked_additions = models.ForeignKey('Addition', null=True)

    def get_absolute_url(self):
        return reverse('user_profile',kwargs={'user_profile': self.pk})

    def __str__(self):
        return f'{self.user.username} Profile'





class Rating(models.Model):
    rating = models.FloatField(default=0)
