# info/views.py

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import requests
from datetime import datetime

@api_view(['GET'])
def index(request):
    api_key = 'Neny6OvaMcEsIDSOkh6pycnUnvJKmwD7'
    current_date = datetime.now().strftime('%Y%m%d')
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&searchdate={current_date}&data=AP01'

    response = requests.get(url).json()

    return Response(response)
