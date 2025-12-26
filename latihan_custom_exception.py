# Custom Exceptions
class UmurTidakValidError(Exception):
    """Kesalahan untuk umur yang tidak masuk akal."""
    pass


class UmurTerlaluMudaError(Exception):
    """Kesalahan jika umur terlalu muda."""
    pass


class UmurTerlaluTuaError(Exception):
    """Kesalahan jika umur terlalu tua."""
    pass


class AkunTidakDiizinkanError(Exception):
    """Kesalahan jika umur tidak memenuhi syarat pembuatan akun."""
    pass


def set_umur(umur):
    if umur < 0:
        raise UmurTidakValidError("Umur tidak boleh negatif!")
    if umur < 5:
        raise UmurTerlaluMudaError("Umur terlalu muda (minimal 5 tahun).")
    if umur > 100:
        raise UmurTerlaluTuaError("Umur terlalu tua (maksimal 100 tahun).")
    return umur


def daftar_akun(umur):
    if umur < 18:
        raise AkunTidakDiizinkanError(
            "Akun tidak dapat dibuat. Umur minimal 18 tahun."
        )
    return "Akun berhasil didaftarkan!"


if __name__ == "__main__":
    while True:
        try:
            u = int(input("Masukkan umur: "))
            umur = set_umur(u)
            print("Umur valid:", umur)
            break
        except ValueError:
            print("Input harus berupa bilangan bulat!")
        except (UmurTidakValidError, UmurTerlaluMudaError, UmurTerlaluTuaError) as e:
            print(e)

    # Coba daftar akun
    try:
        hasil = daftar_akun(umur)
        print(hasil)
    except AkunTidakDiizinkanError as e:
        print(e)
