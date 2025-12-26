class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur} tahun"


class Mahasiswa(Person):
    def __init__(self, nama, umur, nim):
        # Memanggil constructor dari parent class (Person)
        super().__init__(nama, umur)
        self.nim = nim

    def info(self):
        return f"Mahasiswa: {self.nama}, Umur: {self.umur}, NIM: {self.nim}"


# Instansiasi objek
p = Person("Andi", 30)
m = Mahasiswa("Budi", 20, "20241001")

# Memanggil method info()
print(p.info())
print(m.info())