
data = [['Nama','NIM','Tempat Lahir', 'Tanggal Lahir', 'Angkatan'],
       ['Irsyad','0048371345','Ternate','14','2020']]

def main():
    
    programMenyala = True
    listMenu()
    while (programMenyala):
        print("/n")
        pilihMenu = input("Masukan Menu (nomor): ")
        match pilihMenu:
            case "1":
                tampilData()
            case "2":
                inputMahasiswa()
            case "3":
                hapusMahasiswa()
            # case "4":
            #     update()
            # case "5":
            #     cariBarang()
            # case "6":
            #     exit()
        
    
    
def listMenu():
    print("Menu:")
    print("1. Tampil")
    print("2. Input Mahasiswa")
    print("2. Hapus Mahasiswa")
    print("6. Keluar")
    
def tampilData():
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(f"{data[i][j]:<{15}}" ,end=' ')
        print()
    
def inputMahasiswa():
    inputNamaMahasiswa = input("Masukan Nama Mahasiswa: ")
    inputNIMMahasiswa = input("Masukan NIM Mahasiswa: ")
    inputTempatLahir = input("Masukan Tempat Lahir Mahasiswa: ")
    inputTanggalLahir = input("Masukan Tanggal Lahir Mahasiswa: ")
    inputAngkatan = input("Masukan Angkatan Mahasiswa: ")
    
    dataMasuk = [inputNamaMahasiswa, inputNIMMahasiswa, inputTempatLahir, inputTanggalLahir, inputAngkatan]
    data.append(dataMasuk)
    
def hapusMahasiswa():
    pilihNamaMahasiswa = input("Pilih Nama Mahasiswa: ")
    jumlahIndexTotalMahasiswa = len(data)
    indexDataTerpilih = ''
    kodeDitemukan = False
    
    for i in range(0,jumlahIndexTotalMahasiswa):
        for z in range(5):
            if data[i][z] == pilihNamaMahasiswa:
                dataKode = data[i][0]
                dataNama = data[i][1]
                dataQuantity = data[i][2]
                dataJadwalkeluar = data[i][3]
                dataJadwalMasuk = data[i][4]
                dataTmp = [[dataKode, dataNama, dataQuantity, dataJadwalkeluar, dataJadwalMasuk]]
                for i in range(len(dataTmp)):
                    for j in range(len(dataTmp[i])):
                        print(f"{dataTmp[i][j]:<{15}}" ,end=' ')
                    print()
                # print(tabulate(dataTmp, headers=header, tablefmt="fancy_grid"))
                namaMahasiswaDitemukan = True
                inputQuantityBaru = input       ("Masukan Quantity Baru: ")
                indexDataTerpilih = i
                
    if namaMahasiswaDitemukan:
        data[indexDataTerpilih][2] = inputQuantityBaru + "Kg"
    else:
        print("Kode Tidak Ditemukan")
     
    

if __name__ == "__main__":
    main()