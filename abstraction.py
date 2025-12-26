from abc import ABC, abstractmethod
import math

class Bentuk(ABC):

    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass

class Lingkaran(Bentuk):

    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * (self.jari_jari ** 2)

    def keliling(self):
        return 2 * math.pi * self.jari_jari

class PersegiPanjang(Bentuk):

    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

# Contoh penggunaan
l = Lingkaran(5)
p = PersegiPanjang(4, 3)

print(f"Luas Lingkaran: {l.luas():.2f}")
print(f"Keliling Lingkaran: {l.keliling():.2f}")
print(f"Luas Persegi Panjang: {p.luas()}")
print(f"Keliling Persegi Panjang: {p.keliling()}")