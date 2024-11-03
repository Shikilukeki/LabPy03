# Praktikum 3

Nama: Rifqi Maulana

Nim: 312410529

Kelas : TI.24.A.5

Dosen: Agung Nugroho, S.Kom., M.Kom.,

Mata Kuliah: Bahasa Pemograman

# Latihan 1

Penjelasan : 

```python
from random import random
```
Mengimpor fungsi random dari modul random

```python
angka_acak = []
```
 Mendefinisikan list kosong untuk menyimpan angka acak
 
```python
while len(angka_acak) < 5:  
```
Melakukan loop selama panjang list angka_acak kurang dari 5

```python
for _ in range(1):  
```
Looping satu kali, menandakan satu iterasi untuk mendapatkan angka acak

```python
a = random()
```
Menghasilkan angka acak antara 0.0 dan 1.0

```python
if a < 0.5:  
```
Memeriksa apakah angka acak kurang dari 0.5

```python
angka_acak.append(a)  
```
Jika ya, menambahkan angka tersebut ke dalam list angka_acak

```python
print(a)
```
Mencetak angka yang baru saja ditambahkan

# 

Contoh hasil eksekusi :

![gambar]()

# Latihan 2

Penjelasan :

```python
modal_awal = 100000000  
```
Mendefinisikan modal awal sebesar 100 juta

```python
persentase_laba = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03
```
Mendefinisikan list persentase laba untuk setiap bulan

```python
laba_per_bulan = []
```
Mendefinisikan list kosong untuk menyimpan laba per bulan

```python
bulan = 1
```
Inisialisasi variabel bulan dengan nilai 1

```python
while bulan <= 8:
```
Memulai loop while yang berjalan selama variabel bulan kurang dari atau sama dengan 8

```python
laba = modal_awal * persentase_laba[bulan-1]
```
Menghitung laba untuk bulan saat ini berdasarkan persentase laba yang sesuai

```python
laba_per_bulan.append(laba)
```
Menambahkan laba yang dihitung ke dalam list laba_per_bulan

```python
bulan += 1
```
Menambahkan laba yang dihitung ke dalam list laba_per_bulan

```python
for i in range(8):
```
Memulai loop for yang berjalan dari 0 hingga 7

```python
print(f"Laba bulan ke - {i + 1} sebesar", int(laba_per_bulan[i]))
```
Mencetak laba untuk setiap bulan dalam format yang ditentukan

```python
print("Total laba yang didapat dari 8 bulan adalah", total_laba)
```
Mencetak total laba yang didapat dari 8 bulan

# 

Contoh hasil eksekusi program : 

![Gambar]()

# Latihan 3

Penjelasan : 

```python
saldo = 1000000
```
Menginisialisasi variabel saldo dengan nilai awal 1.000.000

```python
while True:
```
Memulai loop tak terbatas

```python
    print("\nSelamat datang di ATM")  
    print("1. Cek Saldo") 
    print("2. Tarik Tunai")  
    print("3. Keluar")  
```
Mencetak pesan sambutan di ATM
Menampilkan opsi untuk cek saldo
Menampilkan opsi untuk tarik tunai
Menampilkan opsi untuk keluar

```python
if pilihan == '1':  
        print(f"Saldo Anda saat ini: Rp{saldo}")  
```
Jika pengguna memilih opsi 1, mencetak saldo saat ini

```python
elif pilihan == '2':  # Jika pengguna memilih opsi 2
        jumlah = int(input("Masukkan jumlah penarikan: Rp"))
```
Jika pengguna memilih opsi 2, meminta jumlah penarikan dan mengonversi ke integer

```python
if jumlah > saldo:
            print("Saldo tidak mencukupi untuk penarikan tersebut.") 
```
 Jika jumlah penarikan lebih besar dari saldo saat ini, mencetak pesan bahwa saldo tidak mencukupi

```python
else:  
            saldo -= jumlah  # Mengurangi saldo dengan jumlah penarikan
            print(f"Anda telah menarik: Rp{jumlah}")  
            print(f"Saldo Anda saat ini: Rp{saldo}")  
```
Jika jumlah penarikan tidak lebih besar dari saldo saat in, mengurangi saldo dengan jumlah penarikan, lalu mncetak jumlah yang telah ditarik, dan mencetak saldo saat ini setelah penarikan

```python
elif pilihan == '3':  
        print("Terima kasih telah menggunakan ATM. Sampai jumpa!")
        break  
```
Jika pengguna memilih opsi 3, mencetak pesan terima kasih dan selamat tinggal, lalu keluar dari loop

```python
else:  # Jika pengguna memasukkan opsi yang tidak valid
        print("Opsi tidak valid, silakan coba lagi.")  # Mencetak pesan bahwa opsi tidak valid
```
Jika pengguna memasukkan opsi yang tidak valid, lalu mencetak pesan bahwa opsi tidak valid

# 

Contoh hasil eksekusi program :

![Gambar]()
