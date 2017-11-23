'''
Funkcja obliczająca spalane kalorie podczas wykonywania różnych czynności lub ćwiczeń wybieralnych przez użytkownika z rozwijanej listy
Funkcja oparta o wartości MET (źródło: https://sites.google.com/site/compendiumofphysicalactivities/)
W odpowiednio opisanych oknach użytkownik wpisuje swoją całkowitą masę ciała [kg] oraz czas wykonywania czynności / ćwiczenia [min]
Funkcja musi również przyjąc jako wartość wejściową wielkość MET dla czynności wybranej przez użytkownika
W tym celu prawdopodobnie trzeba będzie stworzyć jakąś bazę danych na podstawie wyżej podanego źródła???
'''
def Spalanie(masa, czas, MET):
    spalane_kalorie = MET * (czas / 60) * masa
    '''MET ma jednostkę [kcal/kg/h], ze względu na wygodę użytkownika będzie on podawał czas w minutach, które trzeba przliczyć na godziny'''
    return spalane_kalorie