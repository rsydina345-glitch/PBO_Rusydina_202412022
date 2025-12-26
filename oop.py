# pendekatan oop
class persegi:
    def __init__(self, sisi):
       self.sisi = sisi
    
    def hitung_luas(self):
        return self.sisi * self.sisi
    
    def hitung_keliling(self):
        return 4 * self.sisi
    
#pembuatan object
persegi = persegi(5)
print(f"luas persegi: {persegi.hitung_luas()}")
print(f"keliling persegi:{persegi.hitung_keliling()}")
    