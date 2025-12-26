import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# =========================
# 1. CLASS MAHASISWA
# =========================
class Mahasiswa:
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk

    def info(self):
        return f"{self.nim} - {self.nama} - {self.jurusan} - IPK: {self.ipk}"

    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru

# =========================
# 2. APLIKASI GUI
# =========================
class AplikasiManajemenMahasiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Manajemen Mahasiswa")
        self.root.geometry("900x500")

        # Dictionary of objects (NIM sebagai key)
        self.data_mahasiswa = {}

        self.buat_input()
        self.buat_tombol()
        self.buat_tabel()

    # =========================
    # INPUT DATA
    # =========================
    def buat_input(self):
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack()

        tk.Label(frame, text="NIM").grid(row=0, column=0)
        tk.Label(frame, text="Nama").grid(row=1, column=0)
        tk.Label(frame, text="Jurusan").grid(row=2, column=0)
        tk.Label(frame, text="IPK").grid(row=3, column=0)

        self.entry_nim = tk.Entry(frame, width=30)
        self.entry_nama = tk.Entry(frame, width=30)
        self.entry_jurusan = tk.Entry(frame, width=30)
        self.entry_ipk = tk.Entry(frame, width=30)

        self.entry_nim.grid(row=0, column=1)
        self.entry_nama.grid(row=1, column=1)
        self.entry_jurusan.grid(row=2, column=1)
        self.entry_ipk.grid(row=3, column=1)

    # =========================
    # TOMBOL OPERASI
    # =========================
    def buat_tombol(self):
        frame = tk.Frame(self.root, pady=10)
        frame.pack()

        tk.Button(frame, text="Tambah", command=self.tambah).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Hapus", command=self.hapus).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Update IPK", command=self.update_ipk).grid(row=0, column=2, padx=5)
        tk.Button(frame, text="Cari", command=self.cari).grid(row=0, column=3, padx=5)
        tk.Button(frame, text="Filter Jurusan", command=self.filter_jurusan).grid(row=0, column=4, padx=5)
        tk.Button(frame, text="Rata-rata IPK", command=self.rata_ipk).grid(row=0, column=5, padx=5)
        tk.Button(frame, text="IPK Tertinggi", command=self.ipk_tertinggi).grid(row=0, column=6, padx=5)
        tk.Button(frame, text="Export TXT", command=self.export_data).grid(row=0, column=7, padx=5)

    # =========================
    # TABEL DATA
    # =========================
    def buat_tabel(self):
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(
            frame,
            columns=("NIM", "Nama", "Jurusan", "IPK"),
            show="headings"
        )

        for col in ("NIM", "Nama", "Jurusan", "IPK"):
            self.tree.heading(col, text=col)

        self.tree.pack(fill=tk.BOTH, expand=True)

    # =========================
    # CRUD & FITUR
    # =========================
    def tambah(self):
        nim = self.entry_nim.get()
        nama = self.entry_nama.get()
        jurusan = self.entry_jurusan.get()
        ipk = self.entry_ipk.get()

        if not nim or not nama or not jurusan or not ipk:
            messagebox.showwarning("Error", "Semua field harus diisi")
            return

        try:
            ipk = float(ipk)
            if ipk < 0 or ipk > 4:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Error", "IPK harus 0 - 4")
            return

        if nim in self.data_mahasiswa:
            messagebox.showwarning("Error", "NIM sudah ada")
            return

        mhs = Mahasiswa(nim, nama, jurusan, ipk)
        self.data_mahasiswa[nim] = mhs

        self.tree.insert("", tk.END, values=(nim, nama, jurusan, ipk))
        self.clear_input()

    def hapus(self):
        item = self.tree.selection()
        if not item:
            return

        nim = self.tree.item(item)["values"][0]
        del self.data_mahasiswa[nim]
        self.tree.delete(item)

    def update_ipk(self):
        item = self.tree.selection()
        if not item:
            return

        nim = self.tree.item(item)["values"][0]
        ipk_baru = self.entry_ipk.get()

        try:
            ipk_baru = float(ipk_baru)
        except ValueError:
            messagebox.showwarning("Error", "IPK tidak valid")
            return

        self.data_mahasiswa[nim].update_ipk(ipk_baru)
        self.refresh_table()

    def cari(self):
        keyword = self.entry_nama.get().lower()
        self.tree.delete(*self.tree.get_children())

        for mhs in self.data_mahasiswa.values():
            if keyword in mhs.nama.lower() or keyword in mhs.nim:
                self.tree.insert("", tk.END,
                                 values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    def filter_jurusan(self):
        jurusan = self.entry_jurusan.get().lower()
        self.tree.delete(*self.tree.get_children())

        for mhs in self.data_mahasiswa.values():
            if jurusan == mhs.jurusan.lower():
                self.tree.insert("", tk.END,
                                 values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    def rata_ipk(self):
        if not self.data_mahasiswa:
            return

        total = sum(m.ipk for m in self.data_mahasiswa.values())
        rata = total / len(self.data_mahasiswa)
        messagebox.showinfo("Rata-rata IPK", f"{rata:.2f}")

    def ipk_tertinggi(self):
        if not self.data_mahasiswa:
            return

        mhs = max(self.data_mahasiswa.values(), key=lambda x: x.ipk)
        messagebox.showinfo("IPK Tertinggi", mhs.info())

    def export_data(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt")
        if not file:
            return

        with open(file, "w") as f:
            for mhs in self.data_mahasiswa.values():
                f.write(mhs.info() + "\n")

        messagebox.showinfo("Sukses", "Data berhasil diexport")

    def refresh_table(self):
        self.tree.delete(*self.tree.get_children())
        for mhs in self.data_mahasiswa.values():
            self.tree.insert("", tk.END,
                             values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    def clear_input(self):
        self.entry_nim.delete(0, tk.END)
        self.entry_nama.delete(0, tk.END)
        self.entry_jurusan.delete(0, tk.END)
        self.entry_ipk.delete(0, tk.END)


# =========================
# MAIN PROGRAM
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiManajemenMahasiswa(root)
    root.mainloop()
