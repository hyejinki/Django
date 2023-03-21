from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'calculation/index.html')

def throw(request):
    return render(request, 'calculation/throw.html')

def catch(request):
    number1 = int(request.GET.get('number1'))
    number2 = int(request.GET.get('number2'))
    context = {
        'number1': number1,
        'number2': number2,
        'num1' : number1 - number2,
        'num2' : number1 * number2,
        'num3' : number1 / number2 if number2 != 0 else '',

    }
    return render(request, 'calculation/catch.html', context)