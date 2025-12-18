baris_hapus = int(input("Masukkan nomor baris yang ingin dihapus: "))

with open("data.txt", "r") as file:
    baris = file.readlines()

with open("data.txt", "w") as file:
    for i in range(len(baris)):
        if i != baris_hapus - 1:
            file.write(baris[i])

print(f"Baris ke-{baris_hapus} berhasil dihapus.")
