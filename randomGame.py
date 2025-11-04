import random
import sys
# Menangkap Angka Random Dari 1-6
rn = random.randint(1, 6)
# Anda Memasukan Tebakan Anda
cc = int(input("Masukan Tebakan Anda (0-6): "))
# Logika Penentuan Kemenangan
if cc == 0:
    sys.exit("Anda Memilih Keluar Dari Game") 
elif cc == rn:
    rs = True
elif (cc > 0 and cc <= 6) and cc != rn:
    rs = False
else :
    # Jika Angka Diluar Jangkauan
    sys.exit("Anda Memasukan Angka Diluar Jangkauan")
    
# Menampilkan Hasil Tebakan
print("Angka Tebakan Anda : ", cc)
print("Angka Yang Keluar : ", rn)
# Menampilkan Hasil Kemenangan
if rs == True:
    print("Selamat, Jawaban Anda Benar!!!")
else:
    print("Jawaban Anda Salah, Silahkan Coba Lagi")