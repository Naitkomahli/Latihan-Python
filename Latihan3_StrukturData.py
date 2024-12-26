try:
    print("===============================")
    print("Program Kalkulator UHUY menggunakan fungsi")
    print("===============================")

    print("Masukan angka-angka(dipisahkan dengan spasi) :")
    angka = list(map(int, input().split()))
    # input() digunakan untuk menerima input dari pengguna.
    # .split() memisahkan angka yang diinput berdasarkan spasi.
    # map(int, ...) mengubah elemen string menjadi angka (integer).
    # list(...) mengubah hasil map menjadi list.


    # menemukan angka terbesar
    angka_terbesar = max(angka) 

    # menyimpan hasil kedalam dictionary
    hasil = {"max_angka": angka_terbesar}

    # menampilkan hasil
    print("list angka :", angka)
    print("angka terbesar adalah :", hasil["max_angka"])
    print("list angka (urut) :", sorted(angka))
    print("list angkat (dijumlahkan) :", sum(angka))

except ValueError:
    print("Error: masukan angka yang valid")

except Exception as e:
    print(f"Terjadi Kesalahan : {e}")