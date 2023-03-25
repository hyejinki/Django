from django.shortcuts import render, redirect
from .models import Myapp
from .forms import MyappForm

# Create your views here.
def index(request):
    myapps = Myapp.objects.all()
    context = {
        'myapps':myapps
    }
    return render(request, 'myapps/index.html', context)


def detail(request, pk):
    myapp = Myapp.objects.get(pk=pk)
    context = {
        'myapp':myapp,
    }
    return render(request, 'myapps/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = MyappForm(request.POST, request.FILES)
        if form.is_valid():
            myapp = form.save()
            return redirect('myapps:detail', myapp.pk)
    else:
        form = MyappForm()
    
    context = {'form':form}
    return render(request, 'myapps/create.html', context)

def delete(request, pk):
    myapp = Myapp.objects.get(pk=pk)
    myapp.delete()
    return redirect('myapp:index')


def update(request, pk):
    myapp = Myapp.objects.get(pk=pk)
    if request.method=="POST":
        form = MyappForm(request.POST, request.FILES, instance=myapp)
        if form.is_valid():
            form.save()
    else:
        form = MyappForm(instance=myapp)
    context = {
        'form':form, 'myapp' : myapp
    }
    return render*(request, 'myapps/update.html', context)