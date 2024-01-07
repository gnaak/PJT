from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('api/news/<str:query>/', views.newslist, name='newslist') 
    ]
 