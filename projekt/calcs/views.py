from django.shortcuts import render
from .models import Czynnosc
from django.http import HttpResponse

def index(request):
    wszystkieczynnosci = Czynnosc.objects.all()
    return render(request, 'calcs/spalanie.html', {'wszystkieczynnosci': wszystkieczynnosci})

def spalanie(request):
    wszystkieczynnosci = Czynnosc.objects.all()
    MET = float(request.POST['czynnosc'])
    czas = float(request.POST['czas'])
    masa = float(request.POST['masa'])
    spalane_kalorie = MET * (czas / 60) * masa
    zaok_spalane_kalorie = round(spalane_kalorie, 1)
    str_spalane_kalorie = (str(zaok_spalane_kalorie) + ' kcal')
    return render(request, 'calcs/spalanie.html', {'spalane_kalorie': str_spalane_kalorie, 'wszystkieczynnosci': wszystkieczynnosci})
