from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hellofromapp(request):
    return HttpResponse("hello narayan i am from the app")