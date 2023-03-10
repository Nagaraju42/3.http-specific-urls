from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app2(request):
    return HttpResponse('this is first function in app2')