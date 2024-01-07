from django.shortcuts import render, redirect
from .models import Main
from .forms import MainForm
from django.contrib.auth.decorators import login_required


def index(request):
    main = Main.objects.all()
    context = {
        'main': main,
    }
    return render(request, 'main/base.html', context)





def sum(request):
    main = Main.objects.all()
    context = {
        'main': main,
    }
    return render(request, 'main/sum.html', context)


def problem2(request):

    return render(request, "problem2.html")

def problem3(request):

    return render(request, "problem3.html")

def problem4(request):
   
    return render(request, 'problem4.html')


