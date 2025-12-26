class Mahasiswa:

    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        return f"Nama: {self.nama}, Nilai: {self.nilai}"

    def __gt__(self, other):
        return self.nilai > other.nilai

    def __eq__(self, other):
        # c. Dua mahasiswa sama jika nilainya sama
        return self.nilai == other.nilai

    def __add__(self, other):
        return self.nilai + other.nilai

    def __mul__(self, faktor):
        return self.nilai * faktor

    def __len__(self):
        # b. Panjang nama mahasiswa
        return len(self.nama)

# d. Contoh penggunaan
m1 = Mahasiswa("Pouster", 80)
m2 = Mahasiswa("Ahmad", 90)
m3 = Mahasiswa("Budi", 80)

# Representasi string
print(m1)
print(m2)
print(m3)

# Panjang nama
print("Panjang nama Pouster:", len(m1))

# Perbandingan kesetaraan nilai
print("Apakah m1 == m3?", m1 == m3)
print("Apakah m1 == m2?", m1 == m2)

# Operasi matematika
print("Total nilai m1 + m2:", m1 + m2)
print("Nilai m1 x 2:", m1 * 2)

# Pengurutan tanpa __lt__
list_mahasiswa = [m1, m2, m3]
hasil_sort = sorted(list_mahasiswa, key=lambda x: x.nilai)

print("\nMahasiswa setelah diurutkan berdasarkan nilai:")
for mhs in hasil_sort:
    print(mhs)