import random
import time
from halo import Halo

def main():
    programMenyala = True
    while(programMenyala):
        pilihan = input("Selamat Datang di Permainan Lempar Dadu, apakah anda ingin bermain? (ya/tidak): ")
        match pilihan:
            case "ya":
                print("\n")
                spinner = Halo(text='Mesin Sedang Berputar', spinner='dots')

                # Mulai spinner
                spinner.start()

                # Proses yang memakan waktu (misalnya, sleep)
                time.sleep(3)

                # Hentikan spinner setelah proses selesai
                spinner.stop()
                a = random.randint(1, 6)
                b = random.randint(1, 6)
                print(f"Dadu Pertama = {a}")
                print(f"Dadu Kedua = {b}")
                print("--------------------")
                perkalianDadu(a, b)
                tambahDadu(a, b)
                kurangDadu(a, b)
                print("Terimakasih Sudah Bermain")
                print("\n")
            case "tidak":
                programMenyala = False
                print("Terimakasih, silahkan datang kembali.")
                
            case _:
                print("--------------------")
                print("Perintah Tidak Diketahui")
                print("\n")
            
    
def perkalianDadu(daduPertama, daduKedua):
    hasil = daduPertama * daduKedua
    print(f"Hasil Perkalian Dadu = {hasil}")
    
    
def tambahDadu(daduPertama, daduKedua):
    hasil = daduPertama + daduKedua
    print(f"Hasil Pertambahan Dadu = {hasil}")
    
def kurangDadu(daduPertama, daduKedua):
    hasil = daduPertama - daduKedua
    print(f"Hasil Pengurangan Dadu = {hasil}")

if __name__ == "__main__":
    main()
    