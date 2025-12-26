def operasi():
    print("=== Operasi Matematika Aman ===")
    print("Pilih operasi:")
    print("1. Pembagian")
    print("2. Perkalian")

    pilihan = input("Masukkan pilihan (1/2): ").strip()
    x = input("Masukkan angka pertama: ").strip()
    y = input("Masukkan angka kedua: ").strip()

    try:
        # b. Pesan khusus jika input kosong / tekan Enter
        if x == "" or y == "":
            raise ValueError("Input kosong terdeteksi. Silakan masukkan angka!")

        a = float(x)
        b = float(y)

        # c. Validasi angka harus positif
        if a < 0 or b < 0:
            raise ValueError("Angka negatif tidak diperbolehkan!")

        if pilihan == "1":
            # PEMBAGIAN
            hasil = a / b  # bisa memunculkan ZeroDivisionError
        elif pilihan == "2":
            # PERKALIAN
            hasil = a * b
        else:
            raise ValueError("Pilihan operasi tidak valid. Gunakan 1 atau 2.")

    except ValueError as ve:
        print("Input salah:", ve)

    except ZeroDivisionError:
        print("Kesalahan: penyebut tidak boleh nol!")

    except Exception as e:
        print("Terjadi kesalahan lain:", e)

    else:
        # d. Hanya tampil jika tidak ada exception
        print(f"Hasil operasi: {hasil}")

    finally:
        # e. Selalu dijalankan
        print("Selesai memproses input.")

if __name__ == "__main__":
    operasi()
