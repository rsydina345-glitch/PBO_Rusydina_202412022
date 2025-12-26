# ======================
# CLASS PARENT
# ======================
class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def info_gaji(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji Pokok: Rp{self.gaji_pokok}")


# ======================
# CHILD CLASS: MANAGER
# ======================
class Manager(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan

    def info_gaji(self):
        total_gaji = self.gaji_pokok + self.tunjangan
        print(f"Nama: {self.nama} (Manager)")
        print(f"Gaji Pokok: Rp{self.gaji_pokok}")
        print(f"Tunjangan: Rp{self.tunjangan}")
        print(f"Gaji Total: Rp{total_gaji}")
        print("-" * 30)


# ======================
# CHILD CLASS: PROGRAMMER
# ======================
class Programmer(Karyawan):
    def __init__(self, nama, gaji_pokok, bonus):
        super().__init__(nama, gaji_pokok)
        self.bonus = bonus

    def info_gaji(self):
        total_gaji = self.gaji_pokok + self.bonus
        print(f"Nama: {self.nama} (Programmer)")
        print(f"Gaji Pokok: Rp{self.gaji_pokok}")
        print(f"Bonus: Rp{self.bonus}")
        print(f"Gaji Total: Rp{total_gaji}")
        print("-" * 30)


# ======================
# COMPOSITION: DEPARTEMEN
# ======================
class Departemen:
    def __init__(self, nama_departemen):
        self.nama_departemen = nama_departemen
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_karyawan(self):
        print(f"Daftar Karyawan Departemen {self.nama_departemen}")
        print("=" * 30)
        for karyawan in self.daftar_karyawan:
            karyawan.info_gaji()


# ======================
# INSTANSIASI
# ======================
manager1 = Manager("Andi", 8000000, 2000000)
manager2 = Manager("Budi", 8500000, 2500000)

programmer1 = Programmer("Citra", 6000000, 1500000)
programmer2 = Programmer("Dina", 6500000, 1000000)

# ======================
# TAMBAH KE DEPARTEMEN
# ======================
departemen_it = Departemen("IT")
departemen_it.tambah_karyawan(manager1)
departemen_it.tambah_karyawan(manager2)
departemen_it.tambah_karyawan(programmer1)
departemen_it.tambah_karyawan(programmer2)

# ======================
# TAMPILKAN INFO GAJI
# ======================
departemen_it.tampilkan_karyawan()