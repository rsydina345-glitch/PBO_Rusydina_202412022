class Bentuk:
    def luas(self):
        return 0


class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi


class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return 3.14 * self.jari_jari * self.jari_jari


# Polymorphism dalam aksi (seperti hewan_list)
bentuk_list = [
    Bentuk(),
    Persegi(4),
    Lingkaran(7)
]

for b in bentuk_list:
    print("Luas:", b.luas())