from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.http import require_GET


@require_GET
def newslist(request, query):
    # query = request.GET.get('query', '')
    naver_api_url = 'https://openapi.naver.com/v1/search/news.json'
    headers = {
        'X-Naver-Client-Id': settings.NAVER_API_CLIENT_ID,
        'X-Naver-Client-Secret': settings.NAVER_API_CLIENT_SECRET,
    }
    params = {
        'query': query,
    }

    response = requests.get(naver_api_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Failed to fetch news'}, status=500)