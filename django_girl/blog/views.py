from django.shortcuts import render
from django.utils import timezone

from .models import Post


# Create your views here.

def agung(request):
    return render(request, 'blog/agung.html')


def register(request):
    return render(request, 'blog/registrasi.html')

def Login(request):
    return render(request, 'blog/Login.html')
