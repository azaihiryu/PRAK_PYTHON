tg = int(input("Masukkan Nilai : "))
uts = int(input("Masukkan Nilai UTS : "))
uas = int(input("Masukkan Nilai UAS : "))

#Untuk menghitung nilai angka
na = (0.2*tg)+(0.3*uts)+(0.5*uas)

print("Nilai Mata Kuliah = ",na)

#Untuk menghitung nilai Huruf Mutu

if na == 100:
    hm = 'S'
elif na >= 81 :
    hm = 'A'
elif na >= 76 :
    hm = 'B+'
elif na >= 66 :
    hm = 'B'
elif na >= 61 :
    hm = 'C+'
elif na >= 51 :
    hm = 'C'
else :
    hm = 'D'

print("Nilai Huruf Mutu : ",hm)


