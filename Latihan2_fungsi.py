print("===============================")
print("Program Kalkulator UHUY menggunakan fungsi")
print("===============================")

#pendefinisian fungsi
def tambah(angka1, angka2):
    return angka1 + angka2

def kurang(angka1, angka2):
    return angka1 - angka2

def kali(angka1, angka2):
    return angka1 * angka2

def bagi(angka1, angka2):
    if angka2 !=0:
        return angka1 / angka2
    else:
        return print("Pembagian error: tidak bisa membagi dengan angka 0")
    
def pangkat(angka1, angka2):
    return angka1 ** angka2

def modulus(angka1, angka2):
    if angka2 != 0:
        return angka1 % angka2
    else:
        return "Error: Modulus dengan nol tidak diperbolehkan!"

#input dari pengguna
angka1 = float(input("Masukan angka pertama :"))
angka2 = float(input("Masukan angka kedua :"))

print("===============================")

#hasil 
print("Hasil penjumlahan", tambah(angka1,angka2))
print("Hasil pengurangan", kurang(angka1,angka2))
print("Hasil perkalian", kali(angka1,angka2))
print("Hasil pembagian", bagi(angka1,angka2))
print("Hasil pangkat", pangkat(angka1,angka2))
print("Hasil modul", modulus(angka1, angka2))

print("===============================")


