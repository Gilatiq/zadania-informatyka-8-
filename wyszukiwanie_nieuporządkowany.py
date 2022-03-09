N = 5
a = [0] * N
def wprowadz_dane():
    for i in range(N):
        a[i] = int(input("Podaj liczbę: "))
def wyprowadz_dane():
    for i in range(N):
        print(a[i])

def wyszukaj_dana (wartosc):
    for i in range(N):
        if a[i] == wartosc:
            return i
    return -1

wprowadz_dane ()
print ("Wprowadzone dane: ")
wyprowadz_dane ()
wartosc = int(input ("Podaj daną do wyszukania: "))
pozycja = wyszukaj_dana (wartosc)
if pozycja >= 0:
    print("Znaleziono dana", wartosc, "na pozycji", pozycja)
    print("Pozycje liczone są od zera")
else:
    print("Nie znaleziono danej", wartosc)

input("\n\nNaciśnij Enter, aby zakończyć")