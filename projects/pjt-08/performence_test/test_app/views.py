from django.http import JsonResponse
from rest_framework.decorators import api_view
import random
import csv
import numpy as np
import pandas as pd
from django.views.decorators.csrf import csrf_exempt


# A. CSV 데이터를 DataFrame으로 변환 후 반환
@api_view(['GET'])
def read_csv(request):
    df = pd.read_csv('data/test_data.CSV', delimiter=",", encoding='cp949')
    df.dropna(axis=0, inplace=True)
    df.isna().sum()
    data = df.to_dict('records')
    return JsonResponse({'data': data})

# B. 결측치 처리 후 데이터 반환
@api_view(['GET'])
def isna(request):
    df = pd.read_csv('data/test_data_has_null.CSV', delimiter=",", encoding='cp949')
    df.fillna('NULL', inplace=True)
    data = df.to_dict('records')
    return JsonResponse({'data': data})

# C. 알고리즘 구현하기(평균 나이와 가장 비슷한 10명)
global_dataframe = pd.read_csv('data/test_data.CSV', delimiter=",", encoding='cp949')

@api_view(['GET'])
def algo_data(request):
    # 결측치를 제외한 데이터로 DataFrame을 필터링합니다.
    filtered_df = global_dataframe.dropna(subset=['나이'])

    # 평균 나이를 계산합니다.
    mean_age = filtered_df['나이'].mean()

    # 나이와 평균 나이 간의 차이를 계산합니다.
    filtered_df['차이'] = abs(filtered_df['나이'] - mean_age)

    # 차이를 기준으로 데이터를 정렬합니다.
    sorted_df = filtered_df.sort_values(by='차이')

    # 상위 10개 행을 선택하여 새로운 DataFrame을 만듭니다.
    result_df = sorted_df.head(10)
    result_data = result_df.to_dict('records')

    return JsonResponse({'data': result_data})

array_length = 1000
random_range = 5000

@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)
