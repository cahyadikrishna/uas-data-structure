import os
#Inisialisasi
data_mhs = []

#Menu
pilih = "y"
while (pilih == "y"):
    os.system("cls")
    print("=========================================================")
    print("| APLIKASI LAPORAN AKHIR NILAI UAS MATKUL STRUKTUR DATA |")
    print("=========================================================")
    print("| MENU APLIKASI:                                        |")
    print("=========================================================")
    print("|               1. Tampilkan Data                       |")
    print("|               2. Tambahkan Data                       |")
    print("|               3. Urutkan berdasarkan Nama             |")
    print("|               4. Urutkan berdasarkan NIM              |")
    print("|               5. Tampilkan Ranking                    |")
    print("=========================================================")
    pilihan=str(input(("Silakan masukkan 'nomor' pilihan anda: ")))

#Pilihan 1    
    if(pilihan=="1"):
        os.system("cls")
        print("==================")
        print("| DATA MAHASISWA |")
        print("==================")
        #Tampilkan data
        if len(data_mhs) == 0:
            print("\n================================================")
            print("NIM              Nama                Nilai UAS")
            print("================================================")
            print(" Data tidak ditemukan, silahkan tambahkan data! ")
            print("================================================") 
        else:
            print("\n=============================================")
            print("NIM	        Nama                Nilai UAS")
            print("=============================================")
            for i in range(len(data_mhs)) :
                print("%i\t%s\t\t%i"%(data_mhs[i][0],data_mhs[i][1],data_mhs[i][2]))
            print("=============================================") 
        x = input("Tekan 'enter' untuk kembali ke menu utama ")

#Pilihan 2  
    elif(pilihan=="2"):
        os.system("cls")
        print("============================")
        print("| TAMBAHKAN DATA MAHASISWA |")
        print("============================")
        jumlah = int(input('\nJumlah data yang akan dimasukkan: '))
        data_in = [[] for k in range (jumlah)]
        for i in range(jumlah):
            print('\nMasukan data ke %i'%(i+1))
            nim = int(input('NIM: '))
            nama = str(input('Nama: '))
            nilai = int(input('Nilai UAS: '))
            data_in[i].append(nim)
            data_in[i].append(nama)
            data_in[i].append(nilai)
        data_mhs += data_in  
        x = input("Tekan 'enter' untuk kembali ke menu utama ")

#Pilihan 3
    elif(pilihan=="3"):
        os.system("cls")
        print("============================")
        print("| URUTKAN BERDASARKAN NAMA |")
        print("============================")
        pilih_sort=str(input(("Silakan pilih '1' untuk ASC dan '2' untuk DESC: ")))
        if(pilih_sort=="1"):
            nama_asc = sorted(data_mhs, key=lambda x: x[1])
            if len(nama_asc) == 0:
                print("\n================================================")
                print("NIM              Nama                Nilai UAS")
                print("================================================")
                print(" Data tidak ditemukan, silahkan tambahkan data! ")
                print("================================================")
            else:
                print("=============================================")
                print("NIM	        Nama                Nilai UAS")
                print("=============================================")
                for i in range(len(nama_asc)) :
                    print("%i\t%s\t\t%i"%(nama_asc[i][0],nama_asc[i][1],nama_asc[i][2]))
                print("=============================================")

        elif(pilih_sort=="2"):
            nama_desc = sorted(data_mhs, key=lambda x: x[1], reverse = True)
            if len(nama_desc) == 0:
                print("\n================================================")
                print("NIM              Nama                Nilai UAS")
                print("================================================")
                print(" Data tidak ditemukan, silahkan tambahkan data! ")
                print("================================================")    
            else:
                print("=============================================")
                print("NIM	        Nama                Nilai UAS")
                print("=============================================")
                for i in range(len(nama_desc)) :
                    print("%i\t%s\t\t%i"%(nama_desc[i][0],nama_desc[i][1],nama_desc[i][2]))
                print("=============================================")
        x = input("Tekan 'enter' untuk kembali ke menu utama ")
#Pilihan 4
    elif(pilihan=="4"):
        os.system("cls")
        print("===========================")
        print("| URUTKAN BERDASARKAN NIM |")
        print("===========================")
        pilih_sort=str(input(("Silakan pilih '1' untuk ASC dan '2' untuk DESC: ")))
        if(pilih_sort=="1"):
            nim_asc = sorted(data_mhs, key=lambda x: x[0])
            if len(nim_asc) == 0:
                print("\n================================================")
                print("NIM              Nama                Nilai UAS")
                print("================================================")
                print(" Data tidak ditemukan, silahkan tambahkan data! ")
                print("================================================")    
            else:
                print("=============================================")
                print("NIM	        Nama                Nilai UAS")
                print("=============================================")
                for i in range(len(nim_asc)) :
                    print("%i\t%s\t\t%i"%(nim_asc[i][0],nim_asc[i][1],nim_asc[i][2]))
                print("=============================================")

        elif(pilih_sort=="2"):
            nim_desc = sorted(data_mhs, key=lambda x: x[0], reverse = True)
            if len(nim_desc) == 0:
                print("\n================================================")
                print("NIM              Nama                Nilai UAS")
                print("================================================")
                print(" Data tidak ditemukan, silahkan tambahkan data! ")
                print("================================================")    
            else:
                print("=============================================")
                print("NIM	        Nama                Nilai UAS")
                print("=============================================")
                for i in range(len(nim_desc)) :
                    print("%i\t%s\t\t%i"%(nim_desc[i][0],nim_desc[i][1],nim_desc[i][2]))
                print("=============================================")
                          
        x = input("Tekan 'enter' untuk kembali ke menu utama ")

#Pilihan 5
    elif(pilihan=="5"):
        os.system("cls")
        print("==========================")
        print("| DATA RANKING MAHASISWA |")
        print("==========================")
        nilai_desc = sorted(data_mhs, key=lambda x: x[2], reverse = True)
        if len(nilai_desc) == 0:
            print("\n===========================================================")
            print("NIM	        Nama                Nilai UAS       Ranking")
            print("===========================================================")
            print("      Data tidak ditemukan, silahkan tambahkan data!       ")
            print("===========================================================")    
        else:
            print("===========================================================")
            print("NIM	        Nama                Nilai UAS       Ranking")
            print("===========================================================")
            for i in range(len(nilai_desc)) :
                print("%i\t%s\t\t%i\t\t%i"%(nilai_desc[i][0],nilai_desc[i][1],nilai_desc[i][2],(i+1)))
            print("===========================================================")
               
        x = input("Tekan 'enter' untuk kembali ke menu utama ")
    else:
        pilih="n"
