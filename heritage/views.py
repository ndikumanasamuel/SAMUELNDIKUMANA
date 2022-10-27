from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('you are welcome on the Rwandan cultural website')


def new(request):
    return HttpResponse('this is a new word')
