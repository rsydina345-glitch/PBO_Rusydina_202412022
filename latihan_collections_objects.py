class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info(self):
        return f"{self.judul} - {self.penulis} ({self.tahun})"


# Membuat list of objects (5 buku)
daftar_buku = [
    Buku("Laskar Pelangi", "Andrea Hirata", 2005),
    Buku("Bumi", "Tere Liye", 2014),
    Buku("Negeri 5 Menara", "Ahmad Fuadi", 2009),
    Buku("Hujan", "Tere Liye", 2016),
    Buku("Dilan 1990", "Pidi Baiq", 2014)
]

# Menampilkan semua buku
print("=== Daftar Buku ===")
for buku in daftar_buku:
    print(buku.info())

# Mencari buku berdasarkan penulis
cari_penulis = "Tere Liye"

print(f"\n=== Buku karya {cari_penulis} ===")
for buku in daftar_buku:
    if buku.penulis == cari_penulis:
        print(buku.info())