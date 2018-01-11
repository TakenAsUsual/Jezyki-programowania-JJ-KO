from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def stronaglowna(request):
    return render(request, 'main/index.html')


def rejestracja(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main:konto')
    else:
        form = UserCreationForm()
    return render(request, 'main/rejestracja.html', {'form': form})

def konto(request):
    return render(request, 'main/konto.html')