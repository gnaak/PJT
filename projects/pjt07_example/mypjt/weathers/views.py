from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import requests
from .serializers import WeatherSerializer
from django.http import JsonResponse
from .models import Weather
# Create your views here.

@api_view(['GET'])
def index(request):
    api_key = settings.API_KEY
    city = 'Seoul,KR'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'

    response = requests.get(url).json()

    return Response(response)

@api_view(['GET'])
def save_data(request):
    api_key = settings.API_KEY
    city = 'Seoul,KR'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'

    response = requests.get(url).json()

    for li in response.get('list'):
        print(li)
        save_data = {
            'dt_txt' : li.get('dt_txt'),
            'temp' : li.get('main').get('temp'),
            'feels_like' : li.get('main').get('feels_like'),
        }
        # 저장하기 위해 데이터를 포장 
        serializers = WeatherSerializer(data=save_data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
    # 저장 완료 메시지
    return JsonResponse({'message' : "okay"})

@api_view(['GET'])
def list_data(request):
    weathers = Weather.objects.all()
    # 응답할 수 있는 형태(JSON)로 포장 
    serializer = WeatherSerializer(weathers, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def hot_weathers(request):
    # 1. 데이터를 날리고 나서 포장
    # 2. 포장하면서 데이터를 날리는 경우 
    weathers = Weather.objects.all()
    hot_weathers = []
    for weather in weathers:
        # 섭씨 = 캘빈 - 273.15
        tmp = round(weather.temp - 273.15, 2)
        if tmp > 30 :
            hot_weathers.append(tmp)
    serializer = WeatherSerializer(hot_weathers, many=True)
    return Response(serializer.data)

