from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.'
# 함수 기본 형태

def index(request):
    return HttpResponse("<h1>hello</h1>")