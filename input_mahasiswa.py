data = [['Nama','NIM','Tempat Lahir', 'Tanggal Lahir', 'Angkatan', 'Jurusan'],
       ['Irsyad','6082001153','Ternate','14-01-2002','2020','Administrasi Bisnis']]

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
                print("Program Dimatikan.")
                programMenyala = False
                exit()
            case _:
                print("Perintah Tidak Ditemukan!")


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
    inputJurusan = input("Masukan Jurusan Mahasiswa: ")

    dataMasuk = [inputNamaMahasiswa, inputNIMMahasiswa, inputTempatLahir, inputTanggalLahir, inputAngkatan, inputJurusan]
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
                dataNama = data[i][0]
                dataNIM = data[i][1]
                dataTempatLahir = data[i][2]
                dataTanggalLahir = data[i][3]
                dataAngkatan = data[i][4]
                dataJurusan = data[i][5]
                dataTmp = [[dataNama, dataNIM, dataTempatLahir, dataTanggalLahir, dataAngkatan, dataJurusan]]
                for x in range(len(dataTmp)):
                    for j in range(len(dataTmp[x])):
                        print(f"{dataTmp[x][j]:<{15}}" ,end=' ')
                    print()
                # print(tabulate(dataTmp, headers=header, tablefmt="fancy_grid"))
                namaMahasiswaDitemukan = True
                indexDataTerpilih = i

    if namaMahasiswaDitemukan:
        data.pop(indexDataTerpilih)
        print("Mahasiswa Berhasil Dihapus")
    else:
        print("Kode Tidak Ditemukan")


def updateNamaBaseOnNim():
    print("\n")
    pilihNPMMahasiswa = input("Masukan NIM Mahasiswa: ")
    jumlahIndexTotalBarang = len(data)
    indexDataTerpilih = ''
    kodeDitemukan = False

    for i in range(0,jumlahIndexTotalBarang):
        for z in range(5):
            if data[i][z] == pilihNPMMahasiswa:
                dataNama = data[i][0]
                dataNIM = data[i][1]
                dataTempatLahir = data[i][2]
                dataTanggalLahir = data[i][3]
                dataAngkatan = data[i][4]
                dataJurusan = data[i][5]
                dataTmp = [[dataNama, dataNIM, dataTempatLahir, dataTanggalLahir, dataAngkatan, dataJurusan]]
                for x in range(len(dataTmp)):
                    for j in range(len(dataTmp[x])):
                        print(f"{dataTmp[x][j]:<{15}}" ,end=' ')
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