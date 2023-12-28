from tabulate import tabulate
import time

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
    
    for i in range(0,jumlahIndexTotalBarang):
        print("\n")
        for z in range(5):
            print(data[i][z])
            if data[i][z] == pilihKodeBarang:
                print(tabulate())
            
    
def barangMasuk():
    print("\n")
    inputKodeBarang = input("Masukan Kode Barang: ")
    inputNamaBarang = input("Masukan Nama Barang: ")
    inputQuantityBarang = input("Masukan Quantity Barang: ")
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    indexDataTerakhir = len(data)
    dataMasuk = [inputKodeBarang, inputNamaBarang, inputQuantityBarang, current_time, current_time]
    print(dataMasuk)
    data.append(dataMasuk)

    
    
# def update():
    
# def cariBarang():
    

if __name__ == "__main__":
    main()