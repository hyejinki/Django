from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from .serializers import ArticleListSerializer
from .models import Article, Comment
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# 전제 조회 / 생성
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # GET 이라면
    articles = Article.objects.all()
    # Serializer : 쉽게 말하면 원하는 형태로 포장하는 것
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)



# 상세 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'PUT':
        # article instance를 파라미터로 전달
        serializer = ArticleListSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    article = get_object_or_404(Article, pk=pk)
    serializer = ArticleListSerializer(article)
    return Response(serializer.data)