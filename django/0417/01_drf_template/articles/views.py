from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .models import Article, Comment
from .serializers import ArticleListSerializer, CommentSerializer
# PageNumberPagination : page_size 기반의 pagination
# LimitOffsetPagination : Limit 와 offset 기반으로 pagination
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
@swagger_auto_schema(methods=['POST'], request_body=ArticleListSerializer)
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # # Pagination
    # articles = Article.objects.all()
    # paginator = PageNumberPagination()
    # paginator.page_size = 5   # 한 페이지에 5개씩
    # # pagination 을 한 쿼리셋으로 변경
    # paginated_articles = paginator.paginate_queryset(articles, request)
    # # 해당 쿼리셋을 기준으로 serializer를 만듦
    # serializer = ArticleListSerializer(paginated_articles, many=True)
    # # paginator를 이용하여, pagination이 완료된 결과 반환
    # # return Response(serializer.data)
    # return paginator.get_paginated_response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleListSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['DELETE'])
def article_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)



@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
