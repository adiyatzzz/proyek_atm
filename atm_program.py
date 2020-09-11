import random
import datetime
from customer import Customer

# instansiasi class customer
atm = Customer(id);

# looping pemeriksaan
while True:
    # user memasukkan pin
    id = int(input("Masukkan Pin Anda : "))
    # trial untuk menghitung berapa kali user memasukkan pin
    trial = 0

    # looping verifikasi
    while id != atm.checkPin() and trial < 3:
        id = int(input("Pin anda salah silahkan masukkan lagi: "))
        trial += 1

        if trial == 3:
            print("Error. Silakan ambil kartu dan coba lagi ..")
            exit()

    # looping utama jika lolos looping verifikasi
    while True :
        print("Selamat datang di atm awe ..")
        print("\n1 - Cek Saldo \t 2 - Debet \t 3 -Simpan \t 4 - Ganti Pin \t 5 - Keluar ")
        selectMenu = int(input("\n Silahkan pilih menu : "))

        if selectMenu == 1:
            # tampilkan jumlah saldo
            print("\n Saldo Anda sekarang adalah " + str(atm.checkBalance()) + "\n")
        elif selectMenu == 2:
            # masukkan nominal ang ingin di withdraw
            nominal = float(input("Masukkan nominal Saldo : "))
            # verifikasi withdraw
            verify_withdraw = input("Konfirmasi anda akan melakukan debet dengan nominal berikut ? y/n" + str(nominal) + " ")

            # jika verifikasi = y
            if verify_withdraw == "y":
                print("Saldo awal anda adalah : Rp. " + str(atm.checkBalance()) + " ")
            else:
                break

            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi debet berhasil")
                print("Sisa saldo Anda " + str(atm.checkBalance()))
            else:
                print("Transaksi debet gagal saldo anda kurang")
                print("Silahkan lakukan penambahan nominal saldo")

        elif selectMenu == 3:
            nominal = float(input("Masukkan nominal Saldo : "))
            verify_deposit = input("Konfirmasi anda akan melakukan deposit dengan nominal berikut ? y/n " + str(nominal) + " ")

            if verify_deposit == "y":
                atm.depostiBalance(nominal)
                print("Saldo anda sekarang adalah " + str(atm.checkBalance()) + " ")
            else:
                break
        elif selectMenu == 4:
            current_pin = int(input("Masukkan pin yang anda : "))

            while current_pin != atm.checkPin():
                current_pin = int(input("Pin anda salah silahkan masukkan pin : "))

            updated_pin = int(input("Masukkan pin yang baru : "))
            print("Pin anda berhasil di ganti")

            verify_newpin = int(input("Coba masukkan pin baru : "))

            if verify_newpin == updated_pin:
                atm.pin = verify_newpin
                print("Pin baru anda sukses di ubah \n")
            else:
                print("Pin baru anda gagal diubah \n")
            
        elif selectMenu == 5:
            print("Resi tercetak otomatis saat anda keluar \n harap simpan tanda terima ini \n sebagai bukti transaksi")
            print("No. Record: ", random.randint(10000, 100000))
            print("Tanggal: " , datetime.datetime.now())
            print("Saldo Akhir: ", str(atm.checkBalance()))
            print("Terima kasih telah menggunakan ATM awe")
            exit()
        else:
            print("Maaf menu tidak tersedia")