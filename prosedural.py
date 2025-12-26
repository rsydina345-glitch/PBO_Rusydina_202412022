# pendekatan prosedural
def hitung_luas_persegi(sisi):
    return sisi * sisi
def hitung_keliling_persegi(sisi):
    return 4 * sisi
# pemanggilan fungsi
sisi = 5
luas = hitung_luas_persegi(sisi)
keliling = hitung_keliling_persegi(sisi)

print(f"luas pesergi: {luas}")    
print(f"keliling persegi : {keliling}")