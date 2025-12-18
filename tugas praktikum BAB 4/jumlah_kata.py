def hitung_kata(teks):

    teks = teks.strip()
    
    kata = teks.split()
    
    return len(kata)

kalimat = input("Masukkan sebuah kalimat: ")

jumlah = hitung_kata(kalimat)
print("Jumlah kata:", jumlah)
