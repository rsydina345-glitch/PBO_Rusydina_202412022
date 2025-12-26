from abc import ABC, abstractmethod

# =========================
# 4. Custom Exception
# =========================
class PoinTidakValidError(Exception):
    """Exception untuk poin yang tidak valid."""
    pass

# =========================
# 1. Abstraction
# =========================
class Pengguna(ABC):

    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def akses(self):
        pass

class Member(Pengguna):

    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin

    def akses(self):
        return "Hak akses: Member (akses fitur standar)"

    # =========================
    # 2. Special Methods
    # =========================
    def __str__(self):
        return f"Member: {self.nama} – Poin: {self.poin}"

    def __add__(self, other):
        return self.poin + other.poin

    def __len__(self):
        return len(self.nama)

# =========================
# 3. Exception Handling (Input)
# =========================
def input_poin():
    poin_input = input("Masukkan poin member: ").strip()

    if poin_input == "":
        raise ValueError("Input poin tidak boleh kosong!")

    poin = int(poin_input)

    if poin < 0:
        raise PoinTidakValidError("Poin tidak boleh negatif!")

    return poin

# =========================
# Program Utama
# =========================
if __name__ == "__main__":
    try:
        poin1 = input_poin()
        poin2 = input_poin()

        m1 = Member("Andi", poin1)
        m2 = Member("Budi", poin2)

        # 5. Output yang diminta
        print("\nInfo Member:")
        print(m1)
        print(m2)

        print("\nHak Akses:")
        print(m1.akses())

        print("\nJumlah poin m1 + m2:", m1 + m2)
        print("Panjang nama m1:", len(m1))

    except ValueError as ve:
        print("Kesalahan input:", ve)

    except PoinTidakValidError as pe:
        print("Kesalahan poin:", pe)