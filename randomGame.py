import random # Mengimport Library Random
rs = False # Inisialisasi Variabel Result
out1 = False # Inisialisasi Variabel Output
cnt = 0 # Inisialisasi Variabel Counter
# Looping Selama Result False
while not out1:
    # Menghasilkan Angka Random Antara 1-6
    rn = random.randint(1, 6) 
    # Meminta Inputan Dari User
    cc = int(input("Masukan Tebakan Anda (0-6): "))
    # Mengecek Kondisi Inputan User
    if cc == 0:
        # Keluar Dari Game
        print("Anda Memilih Keluar Dari Game") 
        out1 = True
        continue
    elif cc == rn:
        # Jika Tebakan Benar
        rs = True
    elif (cc > 0 and cc <= 6) and cc != rn:
        # Jika Tebakan Salah
        rs = False
    else :
        # Jika Angka Diluar Jangkauan
        print("Anda Memasukan Angka Diluar Jangkauan")
        continue
    
    # Menampilkan Hasil Tebakan
    print("Angka Tebakan Anda : ", cc)
    print("Angka Yang Keluar : ", rn)
    # Menampilkan Hasil Kemenangan
    if rs == True:
        print("Selamat, Jawaban Anda Benar!!!")
        print("Anda Menebak Sebanyak ", cnt + 1, " Kali")
        cnt = 0
        out1 = bool(input("Apakah Anda Ingin Keluar Dari Game?\n Tekan apapun untuk Mengulang Permainan, Tekan y untuk berhenti ").lower() == 'y')
    else:
        print("Jawaban Anda Salah, Silahkan Coba Lagi")
        cnt += 1
        if cnt == 6:
            print("Anda Salah Menebak Sebanyak 6 Kali, Apakah Anda Ingin Keluar Dari Game?")
            out1 = bool(input("Tekan apapun untuk Mencoba Kembali, Tekan y untuk berhenti ").lower() == 'y')
            cnt = 0
        
print("Terima Kasih Telah Bermain")