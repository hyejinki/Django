from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>hi</h1>")

def templates(request):
    return render(request, 'firstapp/index.html')

def templates1(request):
    # 변수 만들고
    # 템플릿으로 전달 할 수 있다       
    name = '김혜진'
    job = '백슈'
    menus = ['떡볶이', '치킨']
    
    context = {
        'name': name,
        'job' : job,
        'menus' : menus
    }

    #                                        마지막에 딕셔너리 형태로 전달
    return render(request, 'firstapp/first.html', context)
import datetime
def daily(request):


    menus = ['떡볶이', '치킨', '곱창']
    num = [1, 2, 3]
    user = []
    today = datetime.datetime.now()

    context = {
        'menus' : menus,
        'num' : num,
        'user' : user,
        'today':today,

    }
    return render(request, 'firstapp/daily.html', context)
