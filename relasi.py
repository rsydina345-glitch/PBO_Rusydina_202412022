# relasi aggregation
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
        
    # Tambahkan getter untuk daftar_matakuliah agar bisa diakses di report_program
    def daftar_matakuliah(self):
        return self.daftar_matakuliah

# 2. Definisi Kelas Universitas (Relasi Composition)
class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi

# 3. Fungsi Report (Program Utama)
def report_program(prodi: ProgramStudi, semua_mahasiswa: list[Mahasiswa]):
    print(f"Program Studi: {prodi.nama}")
    
    # Ambil kode MK yang ada di Prodi
    mk_prodi = prodi.daftar_matakuliah
    mk_kode_list = [mk.kode for mk in mk_prodi]
    
    # Cetak daftar mata kuliah
    print(f"Matakuliah: {', '.join(mk_kode_list) or '-'}")

    print("Mahasiswa dan rata-rata nilai:")
    
    for m in semua_mahasiswa:
        # Filter nilai mahasiswa yang relevan (hanya MK yang ada di Prodi)
        relevan = [n for n in m.daftar_nilai if n.kode_mk in mk_kode_list]
        
        avg = 0
        if relevan:
            # Hitung rata-rata
            avg = sum(n.skor for n in relevan) / len(relevan)
        
        # Cetak NIM, Nama, dan Rata-rata Nilai
        print(f" {m.nim} - {m.nama}: {round(avg, 2)}")
        
    print("-" * 40)

# 4. Blok Eksekusi (Contoh Penggunaan)
if __name__ == "__main__":
    
    # Inisialisasi Universitas dan Prodi
    uni = Universitas("Universitas A")
    prodi_ti = uni.buat_program("Teknik Informatika")

    # Inisialisasi Mata Kuliah
    mk1 = MataKuliah("TI101", "Pemrograman Dasar")
    mk2 = MataKuliah("TI102", "Struktur Data")
    
    # Tambahkan Mata Kuliah ke Prodi
    prodi_ti.tambah_matakuliah(mk1)
    prodi_ti.tambah_matakuliah(mk2)

    # Inisialisasi Mahasiswa
    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")

    # Tambahkan Nilai ke Mahasiswa (Relasi Association)
    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("TI102", 78))
    m2.tambah_nilai(Nilai("TI101", 90))
    
    # Tambahkan Nilai yang tidak ada di Prodi (untuk tes filter/relevan)
    # m1.tambah_nilai(Nilai("FIL201", 95)) # Contoh nilai dari MK lain

    # Panggil fungsi report
    report_program(prodi_ti, [m1, m2])