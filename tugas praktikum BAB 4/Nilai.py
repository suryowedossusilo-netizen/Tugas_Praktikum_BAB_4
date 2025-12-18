
batas_nilai = int(input("Masukkan batas nilai: "))

with open("nilai.csv", "r") as file:
    lines = file.readlines()

print("Mahasiswa dengan nilai di atas", batas_nilai, ":")

for line in lines[1:]:
    nama, nilai = line.strip().split(",")
    nilai = int(nilai)

    if nilai > batas_nilai:
        print(nama)