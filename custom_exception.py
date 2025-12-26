class UmurTidakValidError(Exception):
    """Kesalahan untuk umur yang tidak masuk akal."""
    pass

def set_umur(umur):
    if umur < 0:
        raise UmurTidakValidError("Umur tidak boleh negatif!")
    if umur > 150:
        raise UmurTidakValidError("Umur terlalu besar, periksa kembali input.")
    return umur

if __name__ == "__main__":
    try:
        u = int(input("Masukkan umur: "))
        umur = set_umur(u)
    except ValueError:
        print("Input harus berupa bilangan bulat!")
    except UmurTidakValidError as e:
        print(e)
    else:
        print("Umur berhasil disimpan:", umur)