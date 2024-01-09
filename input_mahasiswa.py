
data = [['Nama','NIM','Tempat Lahir', 'Tanggal Lahir', 'Angkatan'],
       ['Irsyad','0048371345','Ternate','14','2020']]

def main():
    
    programMenyala = True
    
    while (programMenyala):
        print("\n")
        listMenu()
        pilihMenu = input("Masukan Menu (nomor): ")
        match pilihMenu:
            case "1":
                tampilData()
            case "2":
                inputMahasiswa()
            case "3":
                hapusMahasiswa()
            case "4":
                updateNamaBaseOnNim()
            case "5":
                exit()
    
    
def listMenu():
    print("Menu:")
    print("1. Tampil")
    print("2. Input Mahasiswa")
    print("3. Hapus Mahasiswa")
    print("4. Update Nama Mahasiswa")
    print("5. Keluar")
    
def tampilData():
    print("\n")
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(f"{data[i][j]:<{15}}" ,end=' ')
        print()
    
def inputMahasiswa():
    print("\n")
    inputNamaMahasiswa = input("Masukan Nama Mahasiswa: ")
    inputNIMMahasiswa = input("Masukan NIM Mahasiswa: ")
    inputTempatLahir = input("Masukan Tempat Lahir Mahasiswa: ")
    inputTanggalLahir = input("Masukan Tanggal Lahir Mahasiswa: ")
    inputAngkatan = input("Masukan Angkatan Mahasiswa: ")
    
    dataMasuk = [inputNamaMahasiswa, inputNIMMahasiswa, inputTempatLahir, inputTanggalLahir, inputAngkatan]
    data.append(dataMasuk)
    
def hapusMahasiswa():
    print("\n")
    pilihNamaMahasiswa = input("Masukan NIM Mahasiswa yang ingin dihapus: ")
    jumlahIndexTotalMahasiswa = len(data)
    indexDataTerpilih = ''
    namaMahasiswaDitemukan = False
    
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
                indexDataTerpilih = z + 1
                
    if namaMahasiswaDitemukan:
        data.pop(indexDataTerpilih)
        print("Mahasiswa Berhasil Dihapus")
    else:
        print("Kode Tidak Ditemukan")
     
    
def updateNamaBaseOnNim():
    print("\n")
    pilihNIMMahasiswa = input("Masukan NIM Mahasiswa: ")
    jumlahIndexTotalBarang = len(data)
    indexDataTerpilih = ''
    kodeDitemukan = False
    
    for i in range(0,jumlahIndexTotalBarang):
        for z in range(5):
            if data[i][z] == pilihNIMMahasiswa:
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
                kodeDitemukan = True
                inputNamaBaru = input("Masukan Nama Baru: ")
                indexDataTerpilih = i
                
    if kodeDitemukan:
        data[indexDataTerpilih][0] = inputNamaBaru
    else:
        print("Kode Tidak Ditemukan")

    

if __name__ == "__main__":
    main()