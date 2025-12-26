class Kendaraan:
    # Class attribute
    bahan_bakar = "Pertamax"

    # Constructor
    def __init__(self, merk, warna, tahun):
        # Instance attributes
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"Kendaraan {self.merk} warna {self.warna} ({self.tahun})"


# Instansiasi object
kendaraan1 = Kendaraan("Toyota Avanza", "Hitam", 2020)
kendaraan2 = Kendaraan("Honda Beat", "Merah", 2023)

print(kendaraan1.info_kendaraan())
print(kendaraan2.info_kendaraan())
print(f"Bahan Bakar: {Kendaraan.bahan_bakar}")
