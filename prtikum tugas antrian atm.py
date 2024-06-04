import queue
import time
import random


atm_antrian = queue.Queue()

def pengunjung(nomer_pengunjung):
    for i in range(nomer_pengunjung):
        nama_pengunjung=f"pengunjung nomor {i+1}"
        atm_antrian.put(nama_pengunjung)
        print(f"{nama_pengunjung} harap tunggu sebentar ya, antreannya gak panjang koq.")
        time.sleep(random.uniform(0.5,1.5))

def proses_transaksi():
    while not atm_antrian.empty():
        pengunjung_sekarang=atm_antrian.get()
        print(f"{pengunjung_sekarang} Silahkan menuju ke atm untuk melakukan transaksi")
        waktu_transaksi=random.uniform(2, 5)
        time.sleep(waktu_transaksi)
        print(f"{pengunjung_sekarang} sudah melakukan transaksi. silahkan meninggalkan atm.")

nomer_pengunjung=int(input("masukkan batas jumlah pengunjung untuk hari ini: "))

pengunjung(nomer_pengunjung)

proses_transaksi()

print("Antrian selesai!!! semua pelanggan telah melakukan transaksi")
