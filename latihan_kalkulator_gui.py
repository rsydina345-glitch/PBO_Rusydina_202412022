import tkinter as tk
from tkinter import messagebox


class KonversiSuhu:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Suhu")
        self.root.geometry("300x200")

        # Label
        self.label = tk.Label(
            root,
            text="Konversi Celsius ke Fahrenheit",
            font=("Arial", 12)
        )
        self.label.pack(pady=10)

        # Entry input Celsius
        self.entry_celsius = tk.Entry(root, width=25)
        self.entry_celsius.pack(pady=5)
        self.entry_celsius.insert(0, "Masukkan suhu Celsius")

        # Button konversi
        self.button_konversi = tk.Button(
            root,
            text="Konversi",
            command=self.konversi_suhu
        )
        self.button_konversi.pack(pady=5)

        # Label hasil
        self.label_hasil = tk.Label(
            root,
            text="Hasil: -",
            font=("Arial", 11)
        )
        self.label_hasil.pack(pady=10)

    def konversi_suhu(self):
        nilai = self.entry_celsius.get()

        try:
            celsius = float(nilai)
            fahrenheit = (celsius * 9 / 5) + 32
            self.label_hasil.config(
                text=f"Hasil: {fahrenheit:.2f} °F"
            )
        except ValueError:
            messagebox.showwarning(
                "Input Salah",
                "Masukkan angka yang valid!"
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = KonversiSuhu(root)
    root.mainloop()