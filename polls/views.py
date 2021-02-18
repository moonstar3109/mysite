from django.shortcuts import render
from django.http import HttpResponse

def index(requst):
    return HttpResponse("Hello world")
# Create your views here.
