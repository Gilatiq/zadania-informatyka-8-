def maksimum(n):
    for i in range(n):
        a = int(input('Podaj ilczbę:'))
        if i == 0:
            maks =  a
        else:
            if a > maks:
                maks = a
    return maks

liczba_elementow = int(input('Podaj liczbę elementów: '))
najwiekszy = maksimum(liczba_elementow)
print("Maksimum wynosi:", najwiekszy)