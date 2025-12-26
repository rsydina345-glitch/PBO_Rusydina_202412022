class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

    def info(self):
        return f"{self.nama} - {self.email}"


# b. Dictionary menyimpan objek pelanggan (id sebagai key)
data_pelanggan = {
    "C001": Pelanggan("C001", "Andi", "andi@gmail.com"),
    "C002": Pelanggan("C002", "Budi", "budi@gmail.com"),
    "C003": Pelanggan("C003", "Citra", "citra@gmail.com")
}

# c. Fungsi tambah pelanggan
def tambah_pelanggan(data, id_pelanggan, nama, email):
    data[id_pelanggan] = Pelanggan(id_pelanggan, nama, email)


# c. Fungsi hapus pelanggan
def hapus_pelanggan(data, id_pelanggan):
    if id_pelanggan in data:
        del data[id_pelanggan]

# c. Fungsi cari pelanggan
def cari_pelanggan(data, id_pelanggan):
    if id_pelanggan in data:
        return data[id_pelanggan]
    return None

# d. Menampilkan seluruh daftar pelanggan
print("=== Daftar Pelanggan ===")
for id_pelanggan, pelanggan in data_pelanggan.items():
    print(f"{id_pelanggan}: {pelanggan.info()}")

# Contoh tambah pelanggan
tambah_pelanggan(data_pelanggan, "C004", "Dina", "dina@gmail.com")

# Contoh cari pelanggan
cari_id = "C002"
hasil = cari_pelanggan(data_pelanggan, cari_id)

if hasil:
    print(f"\nPelanggan ditemukan: {hasil.info()}")
else:
    print("\nPelanggan tidak ditemukan")

# Contoh hapus pelanggan
hapus_pelanggan(data_pelanggan, "C001")

print("\n=== Daftar Pelanggan Setelah Perubahan ===")
for id_pelanggan, pelanggan in data_pelanggan.items():
    print(f"{id_pelanggan}: {pelanggan.info()}")
