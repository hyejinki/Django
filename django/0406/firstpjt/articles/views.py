from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleModelForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles' : articles}
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'articles': article}
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
        return redirect('articles:detail', pk=article.pk)
    else:
        form = ArticleModelForm()
        context = {
            'form':form,
        }
        return render(request, 'articles/create.html', context)
    

def delete(request, pk):
    article = Article.object.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleModelForm(instance=article)
    context = {
        'form':form,
        'article':article
    }
    return render(request, 'articles/update.html', context)