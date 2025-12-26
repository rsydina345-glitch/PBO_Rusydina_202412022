class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Nama saya {self.nama} dengan NIDN {self.nidn} mengajar mata kuliah {mata_kuliah}"


# Pembuatan object
dsn1 = Dosen("Dr. Andi Wijaya", "082345")
dsn2 = Dosen("Prof. Siti Rahma", "079211")

print(dsn1.ajar_mata_kuliah("Pemrograman Python"))
print(dsn2.ajar_mata_kuliah("Struktur Data"))
