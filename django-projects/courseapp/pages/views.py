from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse('anasayfa')

def iletisim(request):
    return HttpResponse('İletişim sayfası')

def hakkimizda(request):
    return HttpResponse('Hakkımızda sayfası')