from tabulate import tabulate

programMenyala = True
header = ['Kode barang (sku)', 'Nama', 'Quantity', 'Jadwal Keluar', 'Jadwal Masuk']
data = [["SKU01", "Mangga", "10Kg", "Test", "Tost"], ["bast", "bist", 'bust', 'best', 'bost']]
def main():
    while programMenyala:
        print("\n")
        listMenu()
        
        pilihMenu = input("Masukan Menu (nomor): ")
        match pilihMenu:
            case "1":
                tampilData()
            case "2":
                barangKeluar()
            case "3":
                barangMasuk()
            case "4":
                update()
            case "5":
                cariBarang()
            case "6":
                exit()
            
        
def listMenu():
    print("Menu:")
    print("1. Tampil")
    print("2. Barang Keluar")
    print("3. Barang Masuk")
    print("4. Update (kalo sku salah)")
    print("5. Cari")
    print("6. Keluar")
    
def tampilData():
    print(tabulate(data, headers=header, tablefmt="fancy_grid"))
    
def barangKeluar():
    pilihKodeBarang = input("Pilih Kode Barang: ")
    jumlahIndexTotalBarang = len(data)
    indexDataTerpilih = ''
    kodeDitemukan = False
    
    for i in range(0,jumlahIndexTotalBarang):
        for z in range(5):
            if data[i][z] == pilihKodeBarang:
                dataKode = data[i][0]
                dataNama = data[i][1]
                dataQuantity = data[i][2]
                dataJadwalkeluar = data[i][3]
                dataJadwalMasuk = data[i][4]
                dataTmp = [[dataKode, dataNama, dataQuantity, dataJadwalkeluar, dataJadwalMasuk]]
                print(tabulate(dataTmp, headers=header, tablefmt="fancy_grid"))
                kodeDitemukan = True
                inputQuantityBaru = input("Masukan Quantity Baru: ")
                indexDataTerpilih = i
                
    if kodeDitemukan:
        data[indexDataTerpilih][2] = inputQuantityBaru + "Kg"
    else:
        print("Kode Tidak Ditemukan")
        
def barangMasuk():
    print("\n")
    inputKodeBarang = input("Masukan Kode Barang: ")
    inputNamaBarang = input("Masukan Nama Barang: ")
    inputQuantityBarang = input("Masukan Quantity Barang: ")
    inputJadwalMasuk = input("Masukan Jadwal Masuk: ")
    inputJadwalKeluar = input("Masukan Jadwal Keluar: ")
    
    dataMasuk = [inputKodeBarang, inputNamaBarang, inputQuantityBarang+"Kg", inputJadwalKeluar, inputJadwalMasuk]
    data.append(dataMasuk)
    
def update():
    pilihKodeBarang = input("Pilih Kode Barang: ")
    jumlahIndexTotalBarang = len(data)
    indexDataTerpilih = ''
    kodeDitemukan = False
    
    for i in range(0,jumlahIndexTotalBarang):
        for z in range(5):
            if data[i][z] == pilihKodeBarang:
                dataKode = data[i][0]
                dataNama = data[i][1]
                dataQuantity = data[i][2]
                dataJadwalkeluar = data[i][3]
                dataJadwalMasuk = data[i][4]
                dataTmp = [[dataKode, dataNama, dataQuantity, dataJadwalkeluar, dataJadwalMasuk]]
                print(tabulate(dataTmp, headers=header, tablefmt="fancy_grid"))
                kodeDitemukan = True
                inputKodeBaru = input("Masukan Kode Baru: ")
                indexDataTerpilih = i
                
    if kodeDitemukan:
        data[indexDataTerpilih][0] = inputKodeBaru
    else:
        print("Kode Tidak Ditemukan")

    
def cariBarang():
    pilihKodeBarang = input("Pilih Kode atau Nama Barang: ")
    jumlahIndexTotalBarang = len(data)
    
    for i in range(0,jumlahIndexTotalBarang):
        for z in range(5):
            if data[i][z] == pilihKodeBarang :
                dataKode = data[i][0]
                dataNama = data[i][1]
                dataQuantity = data[i][2]
                dataJadwalkeluar = data[i][3]
                dataJadwalMasuk = data[i][4]
                dataTmp = [[dataKode, dataNama, dataQuantity, dataJadwalkeluar, dataJadwalMasuk]]
                print(tabulate(dataTmp, headers=header, tablefmt="fancy_grid"))
    

if __name__ == "__main__":
    main()