print("===============================")
print("Program Kalkulator UHUY")
print("===============================")

#input angka dari pengguna
angka1 = float (input("Masukan angka pertama :"))
angka2 = float (input("Masukan angka kedua :"))

print("================================")

#operasi matematika
print("Hasil Penjumlahan :", angka1 + angka2)
print("Hasil Pengurangan :", angka1 - angka2)
print("Hasil Perkalian :", angka1 * angka2)

#penanganan pembagian 0
if angka2 !=0:
    print("Hasil Pembagian :", angka1/angka2)
else:
    print("Hasil Pembagian Error : Pembagian dengan nol tidak diperbolehkan")
    

