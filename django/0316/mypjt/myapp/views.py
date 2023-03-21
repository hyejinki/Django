from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')


def throw(request):
    return render(request, 'myapp/throw.html')


def catch(request):
    message = request.GET.get('message')
    context  = {
        'message':message
    }
    return render(request, 'myapp/catch.html', context)


def articles(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'myapp/articles.html', context)



def create(request):
    return render(request, 'myapp/create.html')

def delete(request):
    return render(request, 'myapp/delete.html')


# 데이터를 DB에 저장
def new(request):
    # 데이터 받아오기
    title = request.POST.get('title')
    content = request.POST.get('content')
    # DB에 저장
    Article.objects.create(title=title, content=content)
    # 생성 후 전체 목록 리스트로 가야함
    
    # myapp:articles로 요청을 다시 보냄
    return redirect('myapp:articles')

def remv(request):
    id = request.POST.get('id')
    article = Article.objects.get(id=id)
    article.delete()

    return redirect('myapp:articles')