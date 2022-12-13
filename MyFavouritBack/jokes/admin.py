from django.contrib import admin
from .models import Joke, Addition, Profile, Rating
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profi'


class CustomProfile(UserAdmin):
    inlines = (ProfileInLine, )

admin.site.register(Joke)
admin.site.register(Addition)
admin.site.register(Rating)
admin.site.unregister(User)
admin.site.register(User, CustomProfile)