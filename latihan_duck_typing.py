class Laptop:
    def nyalakan(self):
        return "Laptop menyala"

class Smartphone:
    def nyalakan(self):
        return "Smartphone menyala"

def tes_nyala(obj):
    print(obj.nyalakan())

# Duck typing dalam aksi (seperti Burung & Pesawat)
l = Laptop()
s = Smartphone()

tes_nyala(l)
tes_nyala(s)