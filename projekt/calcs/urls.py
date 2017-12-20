from django.urls import path
from . import views

app_name = 'calcs'

urlpatterns = [
    path('', views.index, name='index'),
    path('spalanie-wynik/', views.spalanie, name='spalanie')
]
