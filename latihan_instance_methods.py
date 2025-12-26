class ManajerInventori:
    def __init__(self):
        self.inventori = {}

    def tambah_barang(self, nama, jumlah):
        if jumlah > 0:
            if nama in self.inventori:
                self.inventori[nama] += jumlah
            else:
                self.inventori[nama] = jumlah
            return f"Berhasil tambah {jumlah} {nama}. Stok: {self.inventori[nama]}"
        return "Jumlah barang harus positif"

    def hapus_barang(self, nama, jumlah):
        if nama in self.inventori:
            if 0 < jumlah <= self.inventori[nama]:
                self.inventori[nama] -= jumlah
                if self.inventori[nama] == 0:
                    del self.inventori[nama]
                return f"Berhasil hapus {jumlah} {nama}."
            return "Jumlah tidak valid atau stok kurang"
        return "Barang tidak ditemukan"

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong"
        daftar = "Daftar Inventori:\n"
        for nama, stok in self.inventori.items():
            daftar += f"- {nama}: {stok}\n"
        return daftar


# Testing
inv = ManajerInventori()
print(inv.tambah_barang("Laptop", 5))
print(inv.tambah_barang("Mouse", 10))
print(inv.hapus_barang("Laptop", 2))
print(inv.hapus_barang("Mouse", 3))
print(inv.lihat_inventori())