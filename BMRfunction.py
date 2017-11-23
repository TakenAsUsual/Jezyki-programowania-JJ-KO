'''
Funkcja obliczająca podstawowa przemianę materii (basal metabolic rate), inaczej dzienne zużycie kalorii w podstawowych procesach fizjologicznych
Funkcja jako wartości wejściowe przyjmuje wartości wzrostu [cm], masy [kg] oraz wieku [lata], a także uwzględnia płeć
Uzytkownik wartości te będzie wpisywał w odpowienio opisanych oknach
Użytkownik będzie miał do wyboru z rozwijanego paska jedną z dwóch płci (na razie wartość 0 oznacza płeć żeńską, a wszystkie inne wartości płeć męską)
Zwracana wartość ma jednostkę [kcal/dzień]
Funkcja prawdopodobnie zostanie rozszerzona, poprzez uwzględnienie współczynników, które pozwolą na obliczenia dziennego zapotrzebowania na kalorie w zależności
od zadeklarowanej przez użytkownika dziennej aktywności (np. rodzaj wykonywanej pracy)
'''
def BMR(wzrost, masa, wiek, plec):
    if plec == 0:
        '''Dla kobiet'''
        s = -161
    else:
        '''Dla mężczyzn'''
        s = 5
    '''Równanie Mifflin St Jeor (około 5% dokładniejsze od innych istniejących równań)'''
    p = 10.0 * masa + 6.25 * wzrost - 5.0 * wiek + s
    return p