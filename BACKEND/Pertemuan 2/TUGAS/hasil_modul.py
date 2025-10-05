import penambahan
import pengurangan
import perkalian
import pembagian

# Input dari user
a = int(input("Masukkan angka pertama : "))
b = int(input("Masukkan angka kedua   : "))

# Proses dan output
print(f"\nPenambahan dari {a} dan {b} adalah {penambahan.penambahan(a, b)}")
print(f"Pengurangan dari {a} dan {b} adalah {pengurangan.pengurangan(a, b)}")
print(f"Perkalian dari {a} dan {b} adalah {perkalian.perkalian(a, b)}")
print(f"Pembagian dari {a} dan {b} adalah {pembagian.pembagian(a, b)}")
