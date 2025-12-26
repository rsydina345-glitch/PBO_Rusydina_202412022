# =========================
# RELASI AGGREGATION
# =========================
class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim   
        self.nama = nama
        self.daftar_nilai = []  # agregasi: Nilai dapat berdiri sendiri

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)

    # f. method rata-rata
    def rata_rata(self):
        if not self.daftar_nilai:
            return 0
        return sum(n.skor for n in self.daftar_nilai) / len(self.daftar_nilai)


class MataKuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama


class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = []  # agregasi: MataKuliah dapat berdiri sendiri

    def tambah_matakuliah(self, mk: MataKuliah):
        self.daftar_matakuliah.append(mk)


# =========================
# RELASI COMPOSITION
# =========================
class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi


# =========================
# FUNGSI REPORT
# =========================
def report_program(prodi: ProgramStudi, semua_mahasiswa: list[Mahasiswa]):
    print(f"Program Studi: {prodi.nama}")

    mk_prodi = prodi.daftar_matakuliah
    mk_kode_list = [mk.kode for mk in mk_prodi]

    print(f"Mata Kuliah: {', '.join(mk_kode_list) or '-'}")
    print("Mahasiswa dan rata-rata nilai:")

    for m in semua_mahasiswa:
        relevan = [n for n in m.daftar_nilai if n.kode_mk in mk_kode_list]

        avg = 0
        if relevan:
            avg = sum(n.skor for n in relevan) / len(relevan)

        print(f" {m.nim} - {m.nama}: {round(avg, 2)}")

    print("-" * 40)


# =========================
# BLOK EKSEKUSI
# =========================
if __name__ == "__main__":

    # a. Tambah Program Studi
    uni = Universitas("Universitas A")
    prodi_ti = uni.buat_program("Teknik Informatika")
    prodi_si = uni.buat_program("Sistem Informasi")
    prodi_mi = uni.buat_program("Manajemen Informatika")

    # b. Mata Kuliah tiap Prodi
    prodi_ti.tambah_matakuliah(MataKuliah("TI101", "Pemrograman Dasar"))
    prodi_ti.tambah_matakuliah(MataKuliah("TI102", "Struktur Data"))

    prodi_si.tambah_matakuliah(MataKuliah("SI201", "Basis Data"))
    prodi_si.tambah_matakuliah(MataKuliah("SI202", "Analisis Sistem"))

    prodi_mi.tambah_matakuliah(MataKuliah("MI301", "Aplikasi Perkantoran"))
    prodi_mi.tambah_matakuliah(MataKuliah("MI302", "Manajemen Proyek"))

    # c. Mahasiswa & Nilai
    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")
    m3 = Mahasiswa("23003", "Andi")

    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("TI102", 78))

    m2.tambah_nilai(Nilai("SI201", 90))
    m2.tambah_nilai(Nilai("SI202", 88))

    m3.tambah_nilai(Nilai("MI301", 75))
    m3.tambah_nilai(Nilai("MI302", 80))

    mahasiswa_list = [m1, m2, m3]

    # d. Tampilkan daftar mata kuliah tiap Prodi
    print("=== DAFTAR MATA KULIAH PER PROGRAM STUDI ===")
    for p in uni.programs:
        print(p.nama, ":", [mk.kode for mk in p.daftar_matakuliah])
    print()

    # e. Tampilkan daftar nilai mahasiswa
    print("=== DAFTAR NILAI MAHASISWA ===")
    for m in mahasiswa_list:
        print(m.nim, m.nama, ":", [(n.kode_mk, n.skor) for n in m.daftar_nilai])
    print()

    # f. Rata-rata nilai mahasiswa
    print("=== RATA-RATA NILAI MAHASISWA ===")
    for m in mahasiswa_list:
        print(m.nim, m.nama, ":", round(m.rata_rata(), 2))
    print()

    # g. Panggil report_program
    report_program(prodi_ti, mahasiswa_list)
    report_program(prodi_si, mahasiswa_list)
    report_program(prodi_mi, mahasiswa_list)