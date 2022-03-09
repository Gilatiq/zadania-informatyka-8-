N= 5
a= [0] * N

def wprowadz_dane():
    for i in range(N) :
        a[i] = int(input('podaj liczbe:'))

def wyprowadz_dane():
    for i in range(N):
        print(a[i])

wprowadz_dane()
wyprowadz_dane()

input("\n\nAby zakończyć, naciśnij Enter")
