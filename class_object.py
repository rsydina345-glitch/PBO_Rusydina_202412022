class mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def perkenalan(self):
        return f"halo, saya {self.nama} dengan NIM {self.nim}"
    
# pembuatan object
mhs1 = mahasiswa("Rusydina", "TI001")
mhs2 = mahasiswa("Aulia", "TI002")

print(mhs1.perkenalan()) 
print(mhs2.perkenalan())