import ganjil_genap
import positif_negatif
import nilai_huruf

def main():
    angka = int(input("Masukkan angka: "))
    nilai = int(input("Masukkan nilai ujian: "))

    print(f"\n{angka} adalah {ganjil_genap.ganjil_genap(angka)}")
    print(f"{angka} termasuk bilangan {positif_negatif.positif_negatif(angka)}")
    print(f"Nilai {nilai} setara huruf {nilai_huruf.nilai_huruf(nilai)}")

if __name__ == "__main__":
    main()
