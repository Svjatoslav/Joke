from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index,name='home'),
    path('jokes',views.list_of_jokes,name='jokeslist'),
    path('jokes/<int:post_id>/', views.show_post, name='post')

]
