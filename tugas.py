from datetime import date

# ======================
# CLASS BUKU
# ======================
class Buku:
    def __init__(self, judul, penulis, kode_buku, stok, lokasi_rak):
        # Public
        self.judul = judul
        self.penulis = penulis
        self.kode_buku = kode_buku

        # Protected
        self._stok = stok

        # Private
        self.__lokasi_rak = lokasi_rak

    # Getter & Setter lokasi rak
    def get_lokasi_rak(self):
        return self.__lokasi_rak

    def set_lokasi_rak(self, lokasi):
        self.__lokasi_rak = lokasi

    def tambah_stok(self, jumlah):
        self._stok += jumlah

    def kurangi_stok(self, jumlah):
        if jumlah <= self._stok:
            self._stok -= jumlah
            return True
        return False

    def info_buku(self):
        print(f"Judul: {self.judul}, Penulis: {self.penulis}, Kode: {self.kode_buku}, Stok: {self._stok}")


# ======================
# CLASS PEMINJAMAN
# ======================
class Peminjaman:
    def __init__(self, buku, tanggal_pinjam):
        self.kode_buku = buku.kode_buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = None
        self.status = "Dipinjam"
        self.buku = buku   # Association

    def kembalikan(self, tanggal_kembali):
        self.tanggal_kembali = tanggal_kembali
        self.status = "Dikembalikan"
        self.buku.tambah_stok(1)

    def info_peminjaman(self):
        print(f"Kode Buku: {self.kode_buku}, Tanggal Pinjam: {self.tanggal_pinjam}, "
              f"Tanggal Kembali: {self.tanggal_kembali}, Status: {self.status}")


# ======================
# CLASS ANGGOTA
# ======================
class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam):
        # Public
        self.id_anggota = id_anggota
        self.nama = nama

        # Protected
        self._maks_pinjam = maks_pinjam

        # Private
        self.__status_aktif = True

        # Aggregation
        self.daftar_peminjaman = []

    # Getter & Setter status aktif
    def get_status(self):
        return self.__status_aktif

    def set_status(self, status):
        self.__status_aktif = status

    def pinjam_buku(self, buku):
        if not self.__status_aktif:
            print("Anggota tidak aktif")
            return

        if len(self.daftar_peminjaman) >= self._maks_pinjam:
            print("Melebihi batas peminjaman")
            return

        if buku.kurangi_stok(1):
            peminjaman = Peminjaman(buku, date.today())
            self.daftar_peminjaman.append(peminjaman)
            print(f"{self.nama} berhasil meminjam buku {buku.judul}")
        else:
            print("Stok buku habis")

    def kembalikan_buku(self, peminjaman):
        peminjaman.kembalikan(date.today())
        print(f"{self.nama} mengembalikan buku {peminjaman.kode_buku}")

    def info_anggota(self):
        print(f"ID: {self.id_anggota}, Nama: {self.nama}, Status Aktif: {self.__status_aktif}")


# ======================
# CLASS PERPUSTAKAAN (COMPOSITION)
# ======================
class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tampilkan_buku(self):
        print(f"Daftar Buku Perpustakaan {self.nama}")
        for buku in self.daftar_buku:
            buku.info_buku()


# ======================
# INSTANSIASI
# ======================
# 3 Buku
buku1 = Buku("Python Dasar", "Andi", "B001", 3, "Rak A1")
buku2 = Buku("OOP Python", "Budi", "B002", 2, "Rak A2")
buku3 = Buku("Struktur Data", "Citra", "B003", 1, "Rak B1")

# Perpustakaan
perpus = Perpustakaan("Digital Library")
perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)
perpus.tambah_buku(buku3)

# 2 Anggota
anggota1 = Anggota("A01", "Dina", 2)
anggota2 = Anggota("A02", "Eka", 1)

# Peminjaman
anggota1.pinjam_buku(buku1)
anggota1.pinjam_buku(buku2)
anggota2.pinjam_buku(buku3)

# Pengembalian
anggota1.kembalikan_buku(anggota1.daftar_peminjaman[0])

# ======================
# DEMONSTRASI OUTPUT
# ======================
print("\n--- Informasi Buku ---")
perpus.tampilkan_buku()

print("\n--- Informasi Anggota ---")
anggota1.info_anggota()
anggota2.info_anggota()

print("\n--- Daftar Peminjaman Anggota 1 ---")
for p in anggota1.daftar_peminjaman:
    p.info_peminjaman()

print("\n--- Daftar Peminjaman Anggota 2 ---")
for p in anggota2.daftar_peminjaman:
    p.info_peminjaman()