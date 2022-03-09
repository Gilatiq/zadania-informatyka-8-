liczba = int(input('podaj liczbę: '))

print("Cyfry liczby", liczba, "od ostatniej:")

if liczba == 0:
    print(liczba)
else:
    while liczba != 0:
        cyfra = liczba % 10
        print(cyfra)
        liczba = (liczba - cyfra) // 10

input('\n\nAby zakończyć, naciśnij Enter')