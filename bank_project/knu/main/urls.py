from django.urls import path
from . import views

app_name = 'main'   # 앱을 구분할 필요 없으면 안적어도 됨 
urlpatterns = [
    path('', views.index, name='index'),
    path('sum/', views.sum, name='sum'),
    path('problem2/', views.problem2, name='problem2'),
    path('problem3/', views.problem3, name='problem3'),
    path('problem4/', views.problem4, name='problem4'),
]
