from django.http import HttpResponse
from django.shortcuts import render
from .models import Words


def index(request):
    words = Words.objects.all()
    return render(request, 'index.html', {'words': words})


def new(request):
    return HttpResponse('this is a new word')
