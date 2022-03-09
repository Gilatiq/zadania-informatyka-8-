a = int(input('Podaj pierwszą liczbę:'))
b = int(input('Podaj drugą liczbę:'))

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print('NWD=', a)

input("\n\nAby zakończyć, naciśnij Enter")
