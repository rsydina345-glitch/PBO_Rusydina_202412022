class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    # Constructor
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    # Method perkenalan diri
    def perkenalan_diri(self):
        return (f"Halo, saya {self.nama} (NIM: {self.nim}) "
                f"dari jurusan {self.jurusan} "
                f"Universitas: {Mahasiswa.universitas}. IPK: {self.ipk}")

    # Method update IPK
    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru
        return f"IPK {self.nama} berhasil diperbarui menjadi {self.ipk}"

    # Method predikat kelulusan
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Tidak Lulus"


# ------------------------------------------------
# Instansiasi 3 object Mahasiswa
mhs1 = Mahasiswa("Dina", "202412022", "Informatika", 3.7)
mhs2 = Mahasiswa("lana", "202412044", "Sistem Informasi", 3.0)
mhs3 = Mahasiswa("mark", "202412003", "Teknik", 1.2)

# Demonstrasi semua method
print(mhs1.perkenalan_diri())
print("Predikat:", mhs1.predikat_kelulusan())
print()

print(mhs2.perkenalan_diri())
print("Predikat:", mhs2.predikat_kelulusan())
print()

print(mhs3.perkenalan_diri())
print("Predikat:", mhs3.predikat_kelulusan())
print()

# Update IPK mahasiswa 3 lalu tampilkan predikat baru
print(mhs3.update_ipk(2.7))
print("Predikat baru:", mhs3.predikat_kelulusan())
