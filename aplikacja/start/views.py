from django.shortcuts import render
from django.http import HttpResponse

def f_start(request):
    return render(request, 'start.html')