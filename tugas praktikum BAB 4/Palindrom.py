def cek_palindrom(teks):
    teks_bersih = teks.replace(" ", "").lower()
    return teks_bersih == teks_bersih[::-1]

teks1 = input("Masukkan teks pertama: ")
teks2 = input("Masukkan teks kedua: ")

if cek_palindrom(teks1):
    print(f'"{teks1}" adalah Palindrom')
else:
    print(f'"{teks1}" bukan Palindrom')

if cek_palindrom(teks2):
    print(f'"{teks2}" adalah Palindrom')
else:
    print(f'"{teks2}" bukan Palindrom')
