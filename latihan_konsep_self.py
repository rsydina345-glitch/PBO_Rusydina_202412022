class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa = []

    def tambah_mahasiswa(self, mhs):
        self.mahasiswa.append(mhs)

    def daftar_mahasiswa(self):
        return [m.nama for m in self.mahasiswa]

    # === (a) METHOD BARU ===
    def jumlah_mahasiswa(self):
        return len(self.mahasiswa)


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama


# ==== Contoh penggunaan (b dan c) ====
if __name__ == "__main__":
    # (b) Buat 2 mata kuliah
    mk1 = MataKuliah("TI101", "Pemrograman DasarS")
    mk2 = MataKuliah("TI102", "Sistem Basis Data")

    # Buat 3 mahasiswa
    m1 = Mahasiswa("23061", "rian")
    m2 = Mahasiswa("23032", "lani")
    m3 = Mahasiswa("23013", "rina")

    # Daftarkan mahasiswa ke masing-masing mata kuliah
    mk1.tambah_mahasiswa(m1)
    mk1.tambah_mahasiswa(m2)

    mk2.tambah_mahasiswa(m2)
    mk2.tambah_mahasiswa(m3)

    # (c) Tampilkan daftar mahasiswa & jumlahnya
    print("Mata Kuliah:", mk1.nama)
    print("Daftar mahasiswa:", mk1.daftar_mahasiswa())
    print("Jumlah:", mk1.jumlah_mahasiswa())

    print()

    print("Mata Kuliah:", mk2.nama)
    print("Daftar mahasiswa:", mk2.daftar_mahasiswa())
    print("Jumlah:", mk2.jumlah_mahasiswa())
