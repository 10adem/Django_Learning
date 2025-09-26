from django.http import HttpResponse
from django.urls import path
from . import views

#http://127.0.0.1:8000/client/         => anasayfa
#http://127.0.0.1:8000/client/home     => anasayfa
#http://127.0.0.1:8000/client/kurslar  => kurslar listesi

#http://127.0.0.1:8000/        => anasayfa
#http://127.0.0.1:8000/home     => anasayfa
#http://127.0.0.1:8000/kurslar  => kurslar listesi



urlpatterns = [
    path('', views.kurslar),
    path('list', views.kurslar),
    path('details', views.details),
    path('programlama', views.programlama),
    path('mobil-uygulama', views.mobiluygulama)
]
