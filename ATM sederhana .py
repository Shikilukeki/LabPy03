saldo = 1000000

while True:
    print("\nSelamat datang di ATM")
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Keluar")
    
    pilihan = input("Pilih opsi: ")

    if pilihan == '1':
        print(f"Saldo Anda saat ini: Rp{saldo}")
    elif pilihan == '2':
        jumlah = int(input("Masukkan jumlah penarikan: Rp"))
        if jumlah > saldo:
            print("Saldo tidak mencukupi untuk penarikan tersebut.")
        else:
            saldo -= jumlah
            print(f"Anda telah menarik: Rp{jumlah}")
            print(f"Saldo Anda saat ini: Rp{saldo}")
    elif pilihan == '3':
        print("Terima kasih telah menggunakan ATM. Sampai jumpa!")
        break
    else:
        print("Opsi tidak valid, silakan coba lagi.")
