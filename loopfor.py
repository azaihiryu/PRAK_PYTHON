escaped = False
arr = [] # Inisialisasi arr di luar loop
print(f"Data awal: {arr}")

while not escaped:
    print('\n=== Menu Operasi List ===')
    print('1. Lihat (Menampilkan List)')
    print('2. Tambah (Menambahkan elemen ke akhir)')
    print('3. Hapus Index (Menghapus elemen berdasarkan indeks)')
    print('4. Hapus Nilai (Menghapus semua elemen dengan nilai X)')
    print('0. Keluar (Mengakhiri Program)')
    
    choice = input('Masukkan pilihan Anda: ')
    
    if choice == '1':
        if not arr:
            print('List kosong.')
        else:
            print('Menampilkan isi list' for e in arr)
            print('Isi list saat ini: ')
            for e in arr:
                print(e)
        
    elif choice == '2':
        print('Menambah data...')
        # Konversi input menjadi integer, sesuai dengan data awal di list
        data_to_add = input('Masukkan data integer yang ingin ditambahkan: ')
        arr.append(data_to_add)
        print(f'Data {data_to_add} berhasil ditambahkan. List baru: {arr}')


            
    elif choice == '3':
        print('Menghapus data berdasarkan indeks...')
        if not arr:
            print('List kosong, tidak ada yang bisa dihapus.')
            continue
            
        try:
            # Konversi input indeks menjadi integer untuk fungsi pop()
            index_to_pop = int(input('Masukkan indeks (bilangan bulat) data yang ingin dihapus: '))
            
            # Cek apakah indeks valid
            if 0 <= index_to_pop < len(arr):
                removed_item = arr.pop(index_to_pop)
                print(f'Data di indeks {index_to_pop} ({removed_item}) berhasil dihapus. List baru: {arr}')
            else:
                print('Indeks di luar jangkauan list.')
                
        except ValueError:
            print('Input indeks tidak valid. Harap masukkan bilangan bulat.')
            
    elif choice == '4':
        print('Menghapus semua kemunculan nilai X...')
        try:
            # Konversi input nilai X menjadi integer untuk perbandingan
            x = int(input('Masukkan nilai integer yang ingin dihapus: '))
            
            # Lakukan filtering, pastikan perbandingan antara integer (item) dan integer (x)
            initial_length = len(arr)
            arr = [item for item in arr if item != x]
            
            if len(arr) < initial_length:
                print(f'Semua kemunculan nilai {x} berhasil dihapus. List baru: {arr}')
            else:
                print(f'Nilai {x} tidak ditemukan dalam list.')
                
        except ValueError:
            print('Input nilai X tidak valid. Harap masukkan bilangan bulat.')
            
    elif choice == '0':
        print('Keluar dari program. Sampai jumpa!')
        escaped = True
        
    else:
        print('Pilihan tidak valid, silakan coba lagi.')