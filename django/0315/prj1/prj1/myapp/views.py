from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def detail(request, number):
    context = {
        'number': number,
    }
    return render(request, 'myapp/detail.html', context)


def calc(request, number1, number2):
    context = {
        'number1': number1,
        'number2': number2,
        'num1' : number1 + number2,
        'num2' : number1 - number2,
        'num3' : number1 * number2,
        'num4' : number1 / number2 if number2 != 0 else'',
    }
    return render(request, 'myapp/calc.html', context)


def price(request, thing, num):

    snacks = {
        '칙촉' : 2300,
    }

    context = {
        'thing' : thing,
        'num' : num,
        'price' : num * snacks[thing] if thing in snacks else'',
    }
    return render(request, 'myapp/price.html', context, snacks)