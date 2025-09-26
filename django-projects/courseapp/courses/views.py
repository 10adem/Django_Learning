from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def kurslar(request):
    return HttpResponse('kurslar listesi')

def details(request):
    return HttpResponse('kurs detayları')

def programlama(request):
    return HttpResponse('programlama kursları')

def mobiluygulama(request):
    return HttpResponse('mobil uygulama kursları')

