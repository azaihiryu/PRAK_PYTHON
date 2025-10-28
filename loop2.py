a=0
b=0
c=0
while b >= 0 :
    b = int(input('Masukkan Bilangan : '))
    print(b)
    if b >= 0 :
        a = a+b
        c = c+1
    else :
        break
if c != 0 :
    print('Jumlah nya',a,'\n Rata Rata',a/c,'\n Anda Memasukkan Bilangan Sebanyak',c,'Kali')
else :
    print('Anda hanya memasukan 1 bilangan negatif')