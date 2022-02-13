



from ast import While

from sqlalchemy import true


listBuku = [
    ['A01','2/2/2022','Sindi','Ini Cinta','1'],
    ['B01','12/2/2022','Sari','Kalkulus','1'],
    ['C01','14/2/2022','Asep','Timun Emas','2']
]

listKosong=[]

# menampilkan daftar buku
def menampilkanStokBuku():
    while True:
        stokMenu = input('''
        Daftar Peminjam Buku di Perpustakaan Nadya

        Menu:
        1. Buku yang Dipinjam
        2. Tampilkan Peminjam Buku Tertentu
        3. Kembali Menu Utama
        

        Silakan pilih nomor menu: ''')
    
        if stokMenu == '1':
            if listBuku!= listKosong:
                print('\t------------------Buku yang Dipinjam-------------------\t\t')
                print('Nomor\t| Kode\t| Tanggal\t| Nama\t\t| Judul Buku\t| Jumlah Buku')
                for i in range(len(listBuku)):
                    print(f"{i} \t| {listBuku[i][0]}\t| {listBuku[i][1]}\t| {listBuku[i][2]}\t\t| {listBuku[i][3]}\t| {listBuku[i][4]} ")
                    continue
            elif listBuku == listKosong:
                print('\t\t------Tidak Ada Data------')        
        elif stokMenu == '2':
            if listBuku!= listKosong:
                kodeBuku = input('Masukan Kode Buku:')
                for i in range(len(listBuku)):
                    if kodeBuku == listBuku[i][0]:
                        print(f'Kode Buku: {kodeBuku}')
                        print('\t------------------Buku yang Dipinjam-------------------\t\t')
                        print('Nomor\t| Kode\t| Tanggal\t| Nama\t\t| Judul Buku\t| Jumlah Buku')
                        print(f"{i} \t| {listBuku[i][0]} \t| {listBuku[i][1]}\t| {listBuku[i][2]}\t\t| {listBuku[i][3]}\t| {listBuku[i][4]} ")
                        break
                else:
                    print('\t\t------Tidak Ada Data------')
            elif listBuku == listKosong:
                print('\t\t------Tidak Ada Data------') 
        elif stokMenu == '3':
            kembali = input('Apakah Anda ingin kembali ke Menu Utama?(Ya/No):')
            if kembali == 'Ya':
                menuUtama()
            elif kembali == 'No':
                menampilkanStokBuku()
        else:
            menampilkanStokBuku()

def menambahStokBuku():
    while True:
        tambahStok = input('''
        Menu Menambah Peminjam Buku di Perpustakaan Nadya

        Menu:
        1. Tambah Peminjam Buku Baru
        2. Kembali Menu Utama
        

        Silakan pilih nomor menu: ''')
        if tambahStok == '1':
            kodeBuku0 = input('Masukan Kode Buku:')
            for i in range(len(listBuku)):
                if kodeBuku0 == listBuku[i][0]:
                    print('Sudah Ada')
                    print('\t------------------Buku yang Dipinjam-------------------\t\t')
                    print('Nomor\t| Kode\t| Tanggal\t| Nama\t\t| Judul Buku\t| Jumlah Buku')
                    print(f"{i} \t| {listBuku[i][0]} \t| {listBuku[i][1]}\t| {listBuku[i][2]}\t\t| {listBuku[i][3]}\t| {listBuku[i][4]} ")
                    menambahStokBuku()
            else:
                tanggal = input('Masukan Tanggal:')
                nama = input('Masukan Nama Peminjam:')
                judulBuku = input('Masukan Judul Buku:')
                totalBuku = input('Masukan jumlah buku:')
                while True: 
                    save = input('Apakah Data Akan Disimpan?(Y/N):')
                    if (save =='Y'):
                        listBuku.append([kodeBuku0,tanggal,nama,judulBuku,totalBuku])
                        print('Data Sudah Tersimpan')
                        break
                    elif (save =='N'):
                        menambahStokBuku()
        elif tambahStok == '2':
            kembali = input('Apakah Anda ingin kembali ke Menu Utama?(Ya/No):')
            if kembali == 'Ya':
                menuUtama()
            elif kembali == 'No':
                menambahStokBuku()
        else:
            menambahStokBuku()

def meminjamBuku():
    while True:
        minjamMenu = input('''
        Update Data Peminjaman Buku di Perpustakaan Nadya

        List Menu:
        1. Ubah Data Peminjaman Buku
        2. Kembali Ke Menu Utama
        

        Silakan pilih nomor menu: ''')
    
        if minjamMenu == '1':
            kodeBuku1 = input('Masukan kode buku:')
            for i in range(len(listBuku)):
                if kodeBuku1 == listBuku[i][0]:
                    print('\t------------------Buku yang Dipinjam-------------------\t\t')
                    print('Nomor\t| Kode\t| Tanggal\t| Nama\t\t| Judul Buku\t| Jumlah Buku')
                    print(f"{i} \t| {listBuku[i][0]} \t| {listBuku[i][1]}\t| {listBuku[i][2]}\t\t| {listBuku[i][3]}\t| {listBuku[i][4]} ")
                    while True: 
                        save1 = input('apakah ingin melanjutkan Update data?(Y/N):')
                        if (save1 =='Y'):
                            updateData = input('Masukan kolom/keterangan yang ingin di update:')
                            dataBaru= input(f'Masukan {updateData} Baru:')
                            if updateData == 'Kode':
                                p=0
                                while True:
                                    save2 = input('Apakah ingin melanjutkan Update Data?(Y/N):')
                                    if (save2=='Y'):
                                        listBuku[i][p]= dataBaru
                                        print('Data TerUpdate')
                                        meminjamBuku()
                                    elif (save2 =='N'):
                                        print('Data Tidak TerUpdate')
                                        meminjamBuku()
                            elif updateData == 'Tanggal':
                                p=1
                                while True:
                                    save2 = input('Apakah ingin melanjutkan Update Data?(Y/N):')
                                    if (save2=='Y'):
                                        listBuku[i][p]= dataBaru
                                        print('Data TerUpdate')
                                        meminjamBuku()
                                    elif (save2 =='N'):
                                        print('Data Tidak TerUpdate')
                                        meminjamBuku()
                            elif updateData == 'Nama':
                                p=2
                                while True:
                                    save2 = input('Apakah ingin melanjutkan Update Data?(Y/N):')
                                    if (save2=='Y'):
                                        listBuku[i][p]= dataBaru
                                        print('Data TerUpdate')
                                        meminjamBuku()
                                    elif (save2 =='N'):
                                        print('Data Tidak TerUpdate')
                                        meminjamBuku()
                            elif updateData == 'Judul Buku':
                                p=3
                                while True:
                                    save2 = input('Apakah ingin melanjutkan Update Data?(Y/N):')
                                    if (save2=='Y'):
                                        listBuku[i][p]= dataBaru
                                        print('Data TerUpdate')
                                        meminjamBuku()
                                    elif (save2 =='N'):
                                        print('Data Tidak TerUpdate')
                                        meminjamBuku()
                            elif updateData == 'Jumlah Buku':
                                p=4
                                while True:
                                    save2 = input('Apakah ingin melanjutkan Update Data?(Y/N):')
                                    if (save2=='Y'):
                                        listBuku[i][p]= dataBaru
                                        print('Data TerUpdate')
                                        meminjamBuku()
                                    elif (save2 =='N'):
                                        print('Data Tidak TerUpdate')
                                        meminjamBuku()         
                        elif (save1 =='N'):
                            meminjamBuku()    
            else:
                print('Data yang Anda Cari Tidak Ada')
                meminjamBuku()
        elif minjamMenu == '2':
            kembali = input('Apakah Anda ingin kembali ke Menu Utama?(Ya/No):')
            if kembali == 'Ya':
                menuUtama()
            elif kembali == 'No':
                meminjamBuku()
        else:
            meminjamBuku()
            
def menghapusBuku():
    while True:
        menghapusMenu = input('''
        Menu Menghapus Data Peminjaman Buku

        Menu:
        1. Hapus Data Peminjaman Buku
        2. kembali ke Menu Utama
        

        Silakan pilih nomor menu: ''')
    
        if menghapusMenu == '1':
            kodeBuku2 = input('Masukan Kode Buku:')
            for i in range(len(listBuku)):
                if kodeBuku2 == listBuku[i][0]:
                    print('\t------------------Buku yang Dipinjam-------------------\t\t')
                    print('Nomor\t| Kode\t| Tanggal\t| Nama\t\t| Judul Buku\t| Jumlah Buku')
                    print(f"{i} \t| {listBuku[i][0]} \t| {listBuku[i][1]}\t| {listBuku[i][2]}\t\t| {listBuku[i][3]}\t| {listBuku[i][4]} ")
                    while True: 
                        save1 = input('Apakah Data ingin Dihapus?(Y/N):')
                        if (save1 =='Y'):
                            del listBuku[i]
                            print('Data TerHapus')
                            menghapusBuku()
                        elif (save1 =='N'):
                            print('Data Tidak TerHapus')
                            menghapusBuku()
            else:
                print('Data Tidak Ada')
                menghapusBuku()       

        elif menghapusMenu == '2':
            kembali = input('Apakah Anda ingin kembali ke Menu Utama?(Ya/No):')
            if kembali == 'Ya':
                menuUtama()
            elif kembali == 'No':
                menghapusBuku()
        else:
            menghapusBuku()


        
def menuUtama():
    while True:
        pilihanMenu = input('''
        -----Perpustakaan Nadya----

        List Menu:
        1. Menampilkan Daftar Peminjam Buku
        2. Menambah Data Peminjam Buku 
        3. Mengupdate Peminjaman Buku
        4. Menghapus Daftar Peminjam Buku
        5. Exit Program

        Silakan pilih nomor menu: ''')

        if pilihanMenu == '1':
            menampilkanStokBuku()
        elif pilihanMenu == '2':
            menambahStokBuku()
        elif pilihanMenu == '3':
            meminjamBuku()
        elif pilihanMenu == '4':
            menghapusBuku()
        elif pilihanMenu == '5':
            save1 = input('Apakah Anda Ingin keluar?(Ya/No):')
            if (save1 =='Ya'):
                break
            elif(save1 =='No'):
                print('Pilihan yang Anda Masukkan Salah') 
            menuUtama()
        else:
            menuUtama()

menuUtama()
