b = int(input('Masukkan Bilangan : '))
while (b > 10) | (b < 3) :
    print('Bilangan Maminimal nya 3 dan Maksimal nya 10')
    b = int(input('Masukkan Bilangan : '))
n = 0
a = 1
while n < b:
    n = n+1
    a = a*n
print(a)