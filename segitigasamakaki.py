#Luas = (1/2 alas) * tinggi
#Sisi Miring^2 = (1/2 alas)^2 * tinngi^2
#Keliling = (sm*2) + alas
from cmath import sqrt


a = int(input('Masukkan Alas : '))
t = int(input('Masukan Tinggi : '))
sm = sqrt(pow(a/2,2)+pow(t,2))

L = (a/2)*t
K = (sm*2)+a

print(a)
print(t)
print(sm)
print(L)
print(K)
