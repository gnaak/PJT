from django.shortcuts import render, redirect
from .models import Keyword, Trend
from .forms import KeywordForm, TrendForm
from bs4 import BeautifulSoup
from selenium import webdriver
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Create your views here.

def keyword(request):
    keywords = Keyword.objects.all()
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            # store = form.save(commit=False)
            form.save()
            return redirect('trends:keyword')
    else:
        form = KeywordForm()
    context = {
        'keywords':keywords,
        'form': form,
    }
    return render(request, 'trends/keyword.html', context)

def delete(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')
def crawling(request):
    keywords = Keyword.objects.all()
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trends:crawling')
    else:
        form = KeywordForm()

    num_li = []
    keywords = Keyword.objects.all()
    for keyword in keywords:
        key = keyword.name
        url = f'https://www.google.com/search?q={key}'

        driver = webdriver.Chrome()
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        result_stats = soup.select_one("div#result-stats")
        if result_stats:
            num = result_stats.text.split(' ')[2][:-1]
            num = int(num.replace(',',''))
            num_li.append(num)  # 검색 결과 갯수를 리스트에 저장
        else:
            num = 0  # 검색 결과가 없는 경우 0으로 처리

        # 기존 Trend 객체 업데이트 또는 생성
        trend, created = Trend.objects.get_or_create(name=key, defaults={'result': num, 'search_period': '전체 기간'})

        if not created:
            # 이미 Trend 객체가 존재하는 경우, 결과 갯수와 검색 기간 업데이트
            trend.result = num
            trend.search_period = '전체 기간'
            trend.save()
        driver.quit()

    # zip을 사용하여 키워드와 검색 결과 갯수를 묶어서 템플릿에 전달
    keyword_num_list = zip(keywords, num_li)

    context = {
        'keyword_num_list': keyword_num_list,  # 수정된 부분
        'form': form,
    }
    return render(request, 'trends/crawling.html', context)


def histogram(request):
    num_li = []
    keywords = Keyword.objects.all()
    for keyword in keywords:
        key = keyword.name
        url = f'https://www.google.com/search?q={key}'

        driver = webdriver.Chrome()
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        result_stats = soup.select_one("div#result-stats")
        if result_stats:
            num = result_stats.text.split(' ')[2][:-1]
            num = int(num.replace(',',''))
            num_li.append(num)  # 검색 결과 갯수를 리스트에 저장
        else:
            num = 0  # 검색 결과가 없는 경우 0으로 처리

        # 기존 Trend 객체 업데이트 또는 생성
        trend, created = Trend.objects.get_or_create(name=key, defaults={'result': num, 'search_period': '전체 기간'})

        if not created:
            # 이미 Trend 객체가 존재하는 경우, 결과 갯수와 검색 기간 업데이트
            trend.result = num
            trend.search_period = '전체 기간'
            trend.save()
        driver.quit()
    
    a = 0 
    xtick = []
    value = []
    trends = Trend.objects.all()

    for trend in trends:
        xtick.append(trend.name)
        value.append(trend.result)
        a +=1
    plt.figure(figsize=(10, 6))

    plt.bar(xtick[:a], value, color='blue')
    plt.title("Technology Trend Analysis")
    plt.ylabel('Result')
    plt.xlabel('Keyword')
    plt.grid(True)
    
    # Save the plot to a BytesIO buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()  # Close the plot to clear memory

    # Encode the image to base64
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    # Close the buffer
    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64, {image_base64}'
    }
    return render(request, 'trends/crawling_histogram.html', context)

