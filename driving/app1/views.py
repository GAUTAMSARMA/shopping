from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def g1(request):
    return HttpResponse('HELLO HOW R U')
