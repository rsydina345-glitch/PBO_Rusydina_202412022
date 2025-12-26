class Penulis:
    def __init__(self, nama):
        self.nama = nama

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis   # Composition: Buku memiliki Penulis

    def info(self):
        return f"Buku: {self.judul}, ditulis oleh {self.penulis.nama}"

# Instansiasi objek (seperti Mesin & Mobil)
penulis = Penulis("Andrea Hirata")
buku = Buku("Laskar Pelangi", penulis)

# Akses data penulis dari objek buku
print(buku.info())

# Bisa juga diakses langsung seperti ini:
print("Nama Penulis:", buku.penulis.nama)