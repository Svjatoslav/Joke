from django.contrib import admin
from django.urls import path, include
from .import views
# from .views import ShowProfilePageView, CreateProfilePageView

urlpatterns = [
    path('', views.index,name='home'),
    path('jokes',views.list_of_jokes,name='jokeslist'),
    path('jokes/<int:post_id>/', views.show_post, name='post'),
   # path('jokes/<int:post_id>/', views.rating_upd, name='rating'),
    path('register/', views.RegisterUser.as_view(),name='register'),
    path('login/', views.LoginUser.as_view(),name='login'),
    path('logout/', views.logout_user,name='logout'),
    # path('create_profile_page/',CreateProfilePageView.as_view(), name='create_user_profile'),
    path('user_profile/', views.profile_page, name='user_profile'),
    path(r'^edit/', views.edit, name='edit'),
]
