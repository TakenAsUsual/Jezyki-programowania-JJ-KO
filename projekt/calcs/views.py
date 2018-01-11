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
    zaok_spalane_kalorie = int(spalane_kalorie)
    str_spalane_kalorie = (str(zaok_spalane_kalorie) + ' kcal')
    return render(request, 'calcs/spalanie.html', {'spalane_kalorie': str_spalane_kalorie, 'wszystkieczynnosci': wszystkieczynnosci})

def bmi(request):
    return render(request, 'calcs/bmi.html')

def bmi_wynik(request):
    wzrost = float(request.POST['wzrost'])
    masa = float(request.POST['masa'])
    bmi_wynik = masa / ((wzrost/100) * (wzrost/100))
    zaok_bmi = round(bmi_wynik,1)
    str_bmi = str(zaok_bmi)
    return render(request, 'calcs/bmi.html', {'bmi_wynik': str_bmi})

def bmr(request):
    return render(request, 'calcs/bmr.html')

def bmr_wynik(request):
    wzrost = float(request.POST['wzrost'])
    wiek = float(request.POST['wiek'])
    masa = float(request.POST['masa'])
    plec = int(request.POST['plec'])
    if plec:
        bmr_wynik = int(665.1 + (9.6 * masa) + (1.8 * wzrost) - (4.7 * wiek))
    else:
        bmr_wynik = int(66.5 + (13.7 * masa) + (5 * wzrost) - (6.8 * wiek))
    str_wynik = (str(bmr_wynik) + ' kcal')
    return render(request, 'calcs/bmr.html', {'bmr_wynik': str_wynik})

def makro(request):
    return render(request, 'calcs/makro.html')

def makro_wynik(request):
    bmr = float(request.POST['bmr'])
    masa = float(request.POST['masa'])
    B = int(2.2 * masa)
    T = int((0.225 * bmr) / 9)
    W = int((bmr - 9 * T - 4 * B) / 4)
    makro_wynik = ('Białko: ' + str(B) + 'g, tłuszcze: ' + str(T) + 'g, weglowodany: ' + str(W) + 'g.')
    return render(request, 'calcs/makro.html', {'makro_wynik': makro_wynik})

def tluszcz(request):
    return render(request, 'calcs/tluszcz.html')

def tluszcz_wynik(request):
    op = float(request.POST['op'])
    masa = float(request.POST['masa'])
    plec = int(request.POST['plec'])
    if plec:
        wynik = ((4.15 * op / 2.54) - (0.082 * masa * 2.2) - 76.76) / (masa * 2.2)
    else:
        wynik = ((4.15 * op / 2.54) - (0.082 * masa * 2.2) - 98.42) / masa * 2.2
    a = (op * 4.15) / 2.54
    b = (0.08 * masa * 2.2) + 98.42
    c = (a - b) / (masa * 2.2)
    TT_wynik = round((wynik * 100),1)
    TT_wynik = (str(TT_wynik) + '%')
    return render(request, 'calcs/tluszcz.html', {'TT_wynik': TT_wynik})
