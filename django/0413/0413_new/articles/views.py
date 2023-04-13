from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.
# 전제 조회 / 생성
# @api_view:함수가 API View 로 동작하도록 변환
# - 메소드 제한 기능
# - HttpResponse 대신 Json이나 DRF의 Response객체 반환 가능

@api_view(['GET', 'POST'])
def article_list(request):
    return JsonResponse({ 'message': 'okay' })

# 상세 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    pass