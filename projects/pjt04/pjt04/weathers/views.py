from django.shortcuts import render
import matplotlib.pyplot as plt

# io : 입출력 연산을 위한 Python 표준 라이브러리
# BytesIO : 이진 데이터를 다루기 위한 버퍼를 제공
# 버퍼 : 임시 저장 공간  
# 파일 시스템과 유사하지만,
# 실제로 파일로 만들지 않고 메모리 단에서 작업할 수 있다. 
from io import BytesIO

# 텍스트 <-> 이진 데이터를 변환할 수 있는 모듈 
import base64

# 참고. 터미널 에러
# UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail.  
# PLT를 만드는 곳과 화면에 그리는 곳이 달라서 오류가 날 수 있다! 경고 준다!

# 백엔드를 Agg로 설정하여 해결
plt.switch_backend('Agg')


# # 그래프를 그려볼 것이다!
def index(request):
#     x = [1, 2, 3, 4]
#     y = [2, 4, 8, 16]

#     # 다른 view 함수에서 이미 plt 를 그린 상태에서
#     # 다시 그리는 경우에 대비하여, 초기화를 진행 

#     plt.plot(x, y)
#     plt.title("TEST GRAPH")
#     plt.xlabel('x label')
#     plt.ylabel('y label')

#     # 비어있는 버퍼를 생성
#     buffer = BytesIO()

#     # 버퍼에 그래프를 저장 
#     plt.savefig(buffer, format='png')

#     # 버퍼의 내용을 base64로 인코딩 해주고 사용할 수 있도록 디코딩
#     image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

#     # 버퍼를 닫아줌 
#     buffer.close()

#     # 이미지를 웹 페이지에 표시하기 위해 
#     # URL 형식(주소 형식)으로 만들어진 문자열을 생성 
#     context = {
#         # chart_image : 저장된 이미지의 경로 
#         'chart_image':f'data:image/png;base64,{image_base64}',
#     }

    return render(request, "base.html")


import pandas as pd
csv_path = 'weathers/data/austin_weather.csv'
df = pd.read_csv(csv_path)
def problem1(request):
    context = {
        'df' : df,
    }
    return render(request, 'problem1.html', context)

def problem2(request):
    csv_path = 'weathers/data/austin_weather.csv'
    df = pd.read_csv(csv_path)

    df['Date']=pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    # 최고, 평균, 최저 온도 열 추출
    max_temp = df['TempHighF']
    avg_temp = df['TempAvgF']
    min_temp = df['TempLowF']

    plt.figure(figsize=(10, 6))
    # 최고 온도 그래프
    plt.plot(max_temp, label='High Temperature', marker='', linestyle='-')

    # 평균 온도 그래프
    plt.plot(avg_temp, label='Avgerage Temperature', marker='', linestyle='-')

    # 최저 온도 그래프
    plt.plot(min_temp, label='Low Temperature', marker='', linestyle='-')

    # 그래프에 레이블과 제목 추가
    plt.xlabel('Date')
    plt.ylabel('Temperature (Farenheit)')
    plt.title('Temperature Variation')

    # 범례 추가
    plt.legend()

    plt.grid()

    buffer = BytesIO()

    # 버퍼에 그래프를 저장 
    plt.savefig(buffer, format='png')
    plt.clf()
    # 버퍼의 내용을 base64로 인코딩 해주고 사용할 수 있도록 디코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    # 버퍼를 닫아줌 
    buffer.close()

    # 이미지를 웹 페이지에 표시하기 위해 
    # URL 형식(주소 형식)으로 만들어진 문자열을 생성 
    context = {
        # chart_image : 저장된 이미지의 경로 
        'chart_image':f'data:image/png;base64,{image_base64}',
    }

    return render(request, "problem2.html", context)

def problem3(request):
    csv_path = 'weathers/data/austin_weather.csv'
    df = pd.read_csv(csv_path)

    # 'Date' 열을 날짜 형식으로 변환
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[['Date','TempHighF','TempAvgF','TempLowF']]
    df.set_index('Date', inplace=True)
    
    # 일별 데이터를 월별로 집계하여 평균을 계산
    monthly_avg = df.resample('M').mean()

    monthly_avg_temp_high = monthly_avg['TempHighF']
    monthly_avg_temp_avg = monthly_avg['TempAvgF']
    monthly_avg_temp_low = monthly_avg['TempLowF']

    plt.figure(figsize=(10, 6))

    # 월별 평균 온도 그래프
    plt.plot(monthly_avg_temp_high, label='High Temperature', marker='', linestyle='-')
    plt.plot(monthly_avg_temp_avg, label='Average Temperature', marker='', linestyle='-')
    plt.plot(monthly_avg_temp_low, label='Low Temperature', marker='', linestyle='-')

    # 그래프에 레이블과 제목 추가
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.title('Monthly Average Temperature Variation')

    # 범례 추가
    plt.legend()

    plt.grid()

    buffer = BytesIO()

    # 버퍼에 그래프를 저장 
    plt.savefig(buffer, format='png')
    plt.clf()
    
    # 버퍼의 내용을 base64로 인코딩하여 사용할 수 있도록 디코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    # 버퍼를 닫아줌 
    buffer.close()

    # 이미지를 웹 페이지에 표시하기 위해 
    # URL 형식(주소 형식)으로 만들어진 문자열을 생성 
    context = {
        # chart_image : 저장된 이미지의 경로 
        'chart_image': f'data:image/png;base64,{image_base64}',
    }

    return render(request, "problem3.html", context)

def problem4(request):
    df = pd.read_csv(csv_path)
    df['Events'].replace(' ', 'No Events', inplace=True)
    

    event_list = list(df['Events'])
    new_list = []  # 새로운 리스트

    for item in event_list:
        # 쉼표로 문자열을 분할하고 공백을 제거한 후에 리스트에 추가
        elements = item.split(',')
        elements = [e.strip() for e in elements]
        new_list.extend(elements)

    weather_dict = dict()
    for weather in new_list:
        weather_dict[weather] = weather_dict.get(weather, 0) + 1

    sort_weather = sorted(weather_dict.items(), key=lambda x: x[1], reverse=True)

    plt.clf()

    plt.figure(figsize=(10, 6))
    plt.title("Events Courts")
    plt.ylabel('Count')
    plt.xlabel('Events')
    plt.grid(True)

    # 히스토그램 그리기
    xtick = []
    value = []
    for x, v in sort_weather:
        xtick.append(x)
        value.append(v)

    plt.bar([1,2,3,4,5], value, color='purple')
    plt.xticks([1,2,3,4,5], xtick)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    # 버퍼를 닫아줌
    buffer.close()
    
    context = {
        'chart_image' : f'data:image/png;base64, {image_base64}'
    }

    return render(request, 'problem4.html', context)


