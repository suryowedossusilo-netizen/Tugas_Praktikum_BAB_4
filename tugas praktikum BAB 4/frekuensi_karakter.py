def karakter_terbanyak(teks):
    frekuensi = {}

    for char in teks:
        if char in frekuensi:
            frekuensi[char] += 1
        else:
            frekuensi[char] = 1

    max_char = None
    max_jumlah = 0

    for char in teks:
        if frekuensi[char] > max_jumlah:
            max_jumlah = frekuensi[char]
            max_char = char

    return max_char, max_jumlah

teks = input("Masukkan kalimat: ")

karakter, jumlah = karakter_terbanyak(teks)
print(f"Karakter terbanyak: '{karakter}' muncul {jumlah} kali")
