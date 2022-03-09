a = int(input('Podaj pierwszą liczbę:'))
b = int(input('Podaj drugą liczbę:'))

while b != 0:
    dzielnik = b
    b = a % b
    a = dzielnik

print('NWD =', a)

input('\n\nAby zakończyć, naciśnij Enter')
