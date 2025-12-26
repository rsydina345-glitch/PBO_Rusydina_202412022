class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        # Atribut Public
        self.nim = nim
        self.nama = nama

        # Atribut Protected
        self._semester = semester

        # Atribut Private
        self.__ipk = ipk

    # Getter protected
    def get_semester(self):
        return self._semester

    # Setter protected
    def set_semester(self, semester_baru):
        if semester_baru <= 0:
            raise ValueError("Semester harus lebih dari 0.")
        self._semester = semester_baru

    # Getter private
    def get_ipk(self):
        return self.__ipk

    # Setter private
    def set_ipk(self, ipk_baru):
        if not (0.0 <= ipk_baru <= 4.0):
            raise ValueError("IPK harus di antara 0.0 sampai 4.0.")
        self.__ipk = ipk_baru


# Contoh penggunaan
if __name__ == "__main__":
    mhs1 = Mahasiswa("221001", "Ayu", 2, 3.45)
    mhs2 = Mahasiswa("221002", "Budi", 4, 3.80)

    print("=== Data Mahasiswa Awal ===")
    print(mhs1.nim, mhs1.nama, mhs1.get_semester(), mhs1.get_ipk())
    print(mhs2.nim, mhs2.nama, mhs2.get_semester(), mhs2.get_ipk())

    print("\n=== Data Setelah Perubahan ===")
    # Mengubah semester dan IPK
    mhs1.set_semester(3)
    mhs1.set_ipk(3.60)

    mhs2.set_semester(5)
    mhs2.set_ipk(3.90)

    print(mhs1.nim, mhs1.nama, mhs1.get_semester(), mhs1.get_ipk())
    print(mhs2.nim, mhs2.nama, mhs2.get_semester(), mhs2.get_ipk())
