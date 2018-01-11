from django.urls import path
from . import views

app_name = 'calcs'

urlpatterns = [
    path('spalanie/', views.index, name='spalanie'),
    path('spalanie-wynik/', views.spalanie, name='spalanie_wynik'),
    path('bmi/', views.bmi, name='bmi'),
    path('bmi-wynik/', views.bmi_wynik, name='bmi_wynik'),
    path('bmr/', views.bmr, name='bmr'),
    path('bmr-wynik/', views.bmr_wynik, name='bmr_wynik'),
    path('makro/', views.makro, name='makro'),
    path('makro-wynik/', views.makro_wynik, name='makro_wynik'),
    path('tluszcz/', views.tluszcz, name='tluszcz'),
    path('tluszcz-wynik/', views.tluszcz_wynik, name='tluszcz_wynik'),
]
