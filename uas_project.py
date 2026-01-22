import tkinter as tk
from abc import ABC, abstractmethod

# ================= CUSTOM EXCEPTION =================
class ItemError(Exception):
    pass


# ================= ABSTRACT BASE CLASS =================
class Item(ABC):
    def __init__(self, judul):
        self.judul = judul  # public

    @abstractmethod
    def info(self):
        pass

    def __str__(self):
        return f"Item: {self.judul}"


# ================= INHERITANCE =================
class Buku(Item):
    def __init__(self, judul, penulis):
        super().__init__(judul)
        self._penulis = penulis      # protected
        self.__jenis = "Buku"        # private

    def info(self):
        return f"Buku | Judul: {self.judul}, Penulis: {self._penulis}"

    # getter
    def get_jenis(self):
        return self.__jenis


class Majalah(Item):
    def __init__(self, judul, edisi):
        super().__init__(judul)
        self.edisi = edisi

    def info(self):
        return f"Majalah | Judul: {self.judul}, Edisi: {self.edisi}"


# ================= AGGREGATION =================
class Perpustakaan:
    def __init__(self):
        self.items = []  # collection of objects (list)

    def tambah_item(self, item):
        if not isinstance(item, Item):
            raise ItemError("Objek bukan Item Perpustakaan")
        self.items.append(item)

    def tampilkan_item(self):
        if not self.items:
            return "Belum ada data"
        return "\n".join(item.info() for item in self.items)


# ================= GUI (COMPOSITION) =================
class PerpustakaanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Perpustakaan")

        self.perpustakaan = Perpustakaan()

        # Form input
        tk.Label(root, text="Judul").pack()
        self.entry_judul = tk.Entry(root)
        self.entry_judul.pack()

        tk.Label(root, text="Penulis / Edisi").pack()
        self.entry_keterangan = tk.Entry(root)
        self.entry_keterangan.pack()

        # Button aksi
        tk.Button(root, text="Tambah Buku", command=self.tambah_buku).pack()
        tk.Button(root, text="Tambah Majalah", command=self.tambah_majalah).pack()
        tk.Button(root, text="Tampilkan Data", command=self.tampilkan_data).pack()

        # Area output
        self.output = tk.Text(root, height=10)
        self.output.pack()

    def tambah_buku(self):
        try:
            judul = self.entry_judul.get()
            penulis = self.entry_keterangan.get()
            if not judul or not penulis:
                raise ItemError("Input tidak boleh kosong")

            buku = Buku(judul, penulis)
            self.perpustakaan.tambah_item(buku)
            self.output.insert(tk.END, "Buku berhasil ditambahkan\n")

        except ItemError as e:
            self.output.insert(tk.END, f"Error: {e}\n")

    def tambah_majalah(self):
        try:
            judul = self.entry_judul.get()
            edisi = self.entry_keterangan.get()
            if not judul or not edisi:
                raise ItemError("Input tidak boleh kosong")

            majalah = Majalah(judul, edisi)
            self.perpustakaan.tambah_item(majalah)
            self.output.insert(tk.END, "Majalah berhasil ditambahkan\n")

        except ItemError as e:
            self.output.insert(tk.END, f"Error: {e}\n")

    def tampilkan_data(self):
        self.output.insert(tk.END, self.perpustakaan.tampilkan_item() + "\n")


# ================= MAIN =================
root = tk.Tk()
app = PerpustakaanGUI(root)
root.mainloop()