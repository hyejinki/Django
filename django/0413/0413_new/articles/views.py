from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
# 전제 조회 / 생성
@api_view(['GET', 'POST'])
def article_list(request):
    pass

# 상세 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    pass