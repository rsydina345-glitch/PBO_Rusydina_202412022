import tkinter as tk
from tkinter import messagebox, ttk, simpledialog


# ===== Class Tugas =====
class Tugas:
    def __init__(self, judul, deskripsi, status="Belum Selesai"):
        self.judul = judul
        self.deskripsi = deskripsi
        self.status = status


# ===== Aplikasi GUI =====
class AplikasiManajemenTugas:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Tugas (To-Do List)")
        self.root.geometry("700x400")

        # List of objects
        self.daftar_tugas = []

        # ===== Frame Input =====
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        tk.Label(frame_input, text="Judul Tugas:").grid(row=0, column=0, sticky=tk.W)
        self.entry_judul = tk.Entry(frame_input, width=40)
        self.entry_judul.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Deskripsi:").grid(row=1, column=0, sticky=tk.W)
        self.entry_deskripsi = tk.Entry(frame_input, width=40)
        self.entry_deskripsi.grid(row=1, column=1, padx=5, pady=5)

        # ===== Frame Tombol =====
        frame_tombol = tk.Frame(root, padx=10, pady=10)
        frame_tombol.pack()

        tk.Button(frame_tombol, text="Tambah Tugas", command=self.tambah_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Edit Tugas", command=self.edit_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Hapus Tugas", command=self.hapus_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Tandai Selesai", command=self.tandai_selesai).pack(side=tk.LEFT, padx=5)

        # ===== Frame Tabel =====
        frame_tabel = tk.Frame(root, padx=10, pady=10)
        frame_tabel.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(
            frame_tabel,
            columns=("Judul", "Deskripsi", "Status"),
            show="headings"
        )
        self.tree.heading("Judul", text="Judul")
        self.tree.heading("Deskripsi", text="Deskripsi")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(
            frame_tabel,
            orient=tk.VERTICAL,
            command=self.tree.yview
        )
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # ===== Fitur Tambah =====
    def tambah_tugas(self):
        judul = self.entry_judul.get()
        deskripsi = self.entry_deskripsi.get()

        if judul and deskripsi:
            tugas_baru = Tugas(judul, deskripsi)
            self.daftar_tugas.append(tugas_baru)

            self.tree.insert(
                "",
                tk.END,
                values=(judul, deskripsi, tugas_baru.status)
            )

            self.entry_judul.delete(0, tk.END)
            self.entry_deskripsi.delete(0, tk.END)

            messagebox.showinfo("Sukses", "Tugas berhasil ditambahkan!")
        else:
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")

    # ===== Fitur Hapus =====
    def hapus_tugas(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item[0])
            judul = item["values"][0]

            self.daftar_tugas = [
                t for t in self.daftar_tugas if t.judul != judul
            ]

            self.tree.delete(selected_item[0])
            messagebox.showinfo("Sukses", "Tugas berhasil dihapus!")
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas terlebih dahulu!")

    # ===== Fitur Edit =====
    def edit_tugas(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item[0])
            judul_lama = item["values"][0]

            judul_baru = simpledialog.askstring("Edit", "Judul baru:")
            deskripsi_baru = simpledialog.askstring("Edit", "Deskripsi baru:")

            if judul_baru and deskripsi_baru:
                for tugas in self.daftar_tugas:
                    if tugas.judul == judul_lama:
                        tugas.judul = judul_baru
                        tugas.deskripsi = deskripsi_baru

                self.tree.item(
                    selected_item[0],
                    values=(judul_baru, deskripsi_baru, item["values"][2])
                )
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan diedit!")

    # ===== Fitur Tandai Selesai =====
    def tandai_selesai(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item[0])
            judul = item["values"][0]

            for tugas in self.daftar_tugas:
                if tugas.judul == judul:
                    tugas.status = "Selesai"

            self.tree.item(
                selected_item[0],
                values=(item["values"][0], item["values"][1], "Selesai")
            )
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas terlebih dahulu!")


# ===== Main Program =====
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiManajemenTugas(root)
    root.mainloop()
