from django.contrib.auth import login
from django.urls import path
from . import views

app_name = 'blog_foods'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('accounts/register/',views.register,name='register'),

]