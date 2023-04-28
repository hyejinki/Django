from django.http import JsonResponse
from rest_framework.decorators import api_view
import numpy as np
import pandas as pd


@api_view(['GET'])
def pandas_read(request):
    df = pd.read_csv('data/test_data.CSV', encoding='cp949')
    df.fillna(value='Null', inplace=True)

    data = df.to_dict('records')
    return JsonResponse({'dat': data})




@api_view(['GET'])
def similar_age(request):
    df = pd.read_csv('data/test_data.CSV', encoding='cp949')
   
   # 평균 계산
    mean_age = df['나이'].mean()
    # 평균 나이의 차이 계산
    df['diff'] = abs(df['나이'] - mean_age)
    # diff를 기준으로 정렬
    df = df.sort_values(by='diff')
    df = df.head(10)    

    data = df.to_dict('records')

    return JsonResponse({'dat': data})


