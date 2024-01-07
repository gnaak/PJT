from django.urls import path
from .views import survey, result

app_name = 'mypolls'
urlpatterns = [
    path('survey/', survey, name='survey'),
    path('result/', result, name='result'),
]
