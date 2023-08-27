from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.


def book(request):
    return HttpResponse('{"message":"created first url path"}')
