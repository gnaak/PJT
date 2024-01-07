from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from django.conf import settings
from .serializers import DepositProductsSerializer, DepositOptionSerializer
from django.http import JsonResponse
from .models import DepositProducts, DepositOptions
from rest_framework import status

# Create your views here.
# api_key = 'eda3390f96c04c096b3a72896126fad4'


SP_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'





@api_view(['GET'])
def index(request):
    api_key = 'eda3390f96c04c096b3a72896126fad4'
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()

    return Response(response)


@api_view(['GET'])
# A. 정기예금 상품 목록 및 옵션 목록 저장 
def save_deposit_products(request):
    api_key = 'eda3390f96c04c096b3a72896126fad4'
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()

    for li in response.get("result").get("baseList"):
        save_data = {
            "fin_prdt_cd" : li.get("fin_prdt_cd"),
            "kor_co_nm" : li.get("kor_co_nm"),
            "fin_prdt_nm" : li.get("fin_prdt_nm"),
            "etc_note" : li.get("etc_note"),
            "join_deny" : li.get("join_deny"),
            "join_member" : li.get("join_member"),
            "join_way" : li.get("join_way"),
            "spcl_cnd" : li.get("spcl_cnd"),      
        }
        serializers = DepositProductsSerializer(data=save_data)
        try:
            if serializers.is_valid(raise_exception=True):
                serializers.save()
        except Exception as e:
            print(e)
    
    options = response.get("result").get("optionList")

    for data in options:
        # product = DepositProducts.objects.filter(fin_prdt_cd=data.get('fin_prdt_cd')).pk
        # print(data)
        # print(DepositProducts.objects.filter(fin_prdt_cd=data.get('fin_prdt_cd'))[0].pk)
        save_data = {
            # 'product' : DepositProducts.objects.filter(fin_prdt_cd=data.get('fin_prdt_cd'))[0],
            'product' : DepositProducts.objects.filter(fin_prdt_cd=data.get('fin_prdt_cd'))[0].pk,
            'fin_prdt_cd' : data.get('fin_prdt_cd'),
            'intr_rate_type_nm' : data.get('intr_rate_type_nm'),
            'intr_rate' : data.get('intr_rate') or 0,
            'intr_rate2' : data.get('intr_rate2'),
            'save_trm' : data.get('save_trm'),
        }
        serializer = DepositOptionSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    return JsonResponse({'message' : "okay"})

@api_view(['GET', 'POST'])
def deposit_products(request):
    # B. 전체 정기예금 상품 목록 출력
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        # 응답할 수 있는 형태(JSON)로 포장 
        serializer = DepositProductsSerializer(products, many = True)
        return Response(serializer.data)
    # C. 정기예금 상품 추가하기
    elif request.method == 'POST': 
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
# D. 특정 상품의 옵션 리스트 출력
def deposit_products_options(request, fin_prdt_cd):
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    options = response.get("result").get("optionList")
    for a in range(39):
        product = DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd)[a]
        ppk = DepositProducts.objects.get(pk=product.pk)
        for li in options:
            if li.get("fin_prdt_cd") == fin_prdt_cd:
                save_data = {
                    'fin_prdt_cd' : li.get('fin_prdt_cd'),
                    'intr_rate_type_nm' : li.get('intr_rate_type_nm'),
                    'intr_rate' : li.get('intr_rate'),
                    'intr_rate2' : li.get('intr_rate2'),
                    'save_trm' : li.get('save_trm'),
                }
                serializer = DepositOptionSerializer(data=save_data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save(product=ppk)
                    return Response(serializer.data)
            
@api_view(['GET'])
# E. 금리가 가장 높은 상품의 정보 출력 
def top_rate(request):
          
    options = DepositOptions.objects.all()
    max_rate = 0 
    top_product = None
    for product in options:
        if max_rate < product.intr_rate2:
            max_rate = product.intr_rate2
            top_product = product
    # print(max_rate)
    # print(top_product.pk)
    # print(top_product.product.pk)
    products = DepositProducts.objects.get(pk =top_product.product.pk)

    serializer = DepositProductsSerializer(products)
    serializer2 = DepositOptionSerializer(top_product)
    return Response({'product' :serializer.data, 'options' :serializer2.data})
    
    # for product1 in products:
    #     if product1.pk == top_product.product.pk:
    #         save_data = {
    #             "fin_prdt_cd" :product1.fin_prdt_cd,
    #             "kor_co_nm" :product1.kor_co_nm,
    #             "fin_prdt_nm" :product1.fin_prdt_nm,
    #             "etc_note" :product1.etc_note,
    #             "join_deny" :product1.join_deny,
    #             "join_member" :product1.join_member,
    #             "join_way" :product1.join_way,
    #             "spcl_cnd" :product1.spcl_cnd,
    #         }
    #         serializer = DepositProductsSerializer(data=save_data)
    #         try:
    #             if serializer.is_valid(raise_exception=True):
    #                 serializer.save()
    #         except Exception as e:
    #             print(e)
    # save_data2 = {
    #     'fin_prdt_cd' : top_product.fin_prdt_cd,
    #     'intr_rate_type_nm' : top_product.intr_rate_type_nm,
    #     'intr_rate' : top_product.intr_rate,
    #     'intr_rate2' : top_product.intr_rate2,
    #     'save_trm' :top_product.save_trm,
    # }    
    # serializer2 = DepositOptionSerializer(data=save_data2)
    # try:
    #     if serializer2.is_valid(raise_exception=True):
    #         serializer2.save()
    # except Exception as e:
    #     print(e)
    # return Response({'product' :serializer.data, 'options' :serializer2.data} )