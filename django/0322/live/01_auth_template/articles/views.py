from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
#3 
# from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

#3. 데코레이터 사용
# @login_required

def create(request):
    # 1
    if not request.COOKIES.get('sessionid'):
        return redirect('accounts:login')

    # 2
    # if not request.user.is_authenticated:
    #     return redirect('accounts:login')



    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)

        print(form.data.get('title'))

        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {'form': form}
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {'form': form, 'article': article}
    return render(request, 'articles/update.html', context)
