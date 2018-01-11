from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.stronaglowna, name='index'),
    path('rejestracja/', views.rejestracja, name='rejestracja'),
    path('konto/', views.konto, name='konto'),
]
