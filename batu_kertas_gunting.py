import random

pilihan = ["batu", "kertas", "gunting"]

while true


while True:
    inputan_pengguna = input("\npilihan anda : \nbatu \nkertas \ngunting \nkeluar"



pilihan = ["batu", "kertas", "gunting"]

while True:
    inputan_pengguna = input("\npilihan anda: \nbatu \nkertas \ngunting \nkeluar\n").lower()
    print("pilihan anda", inputan_pengguna + ".")

    if inputan_pengguna == "keluar":
        break
    if inputan_pengguna not in pilihan:
        continue

    nomor_acak = random.randint(0,2)
    #batu: 0, kertas:1, gunting: 2
    pilihan_komputer = pilihan[nomor_acak]

    nomor_acak = random.randint(0,2)
    #batu = 0, kertas = 1, gunting = 2
    pilihan_komputer = pilihan[nomor_acak]


import random

pilihan_pengguna = ["batu", "gunting", "kertas"]

































import random

anda_menang = 0
komputer_menang = 0

pilihan = ["batu", "kertas", "gunting"]

while True:
    inputan_pengguna = input(
        "\npilihan Anda: \n Batu\n kertas\n gunting \n Q untuk keluar: \n\n").lower()
    print("pilihan anda:", inputan_pengguna + ".")
    if inputan_pengguna == "q":
        break

    if inputan_pengguna not in pilihan:
        continue

    nomor_acak = random.randint(0, 2)
    # batu: 0, kertas: 1, gunting: 2
    pilihan_komputer = pilihan[nomor_acak]
    print("komputer memilih", pilihan_komputer + ".")

    if inputan_pengguna == "batu" and pilihan_komputer == "gunting":
        print("Anda menang!")
        anda_menang += 1

    elif inputan_pengguna == "kertas" and pilihan_komputer == "batu":
        print("Anda Menang!")
        anda_menang += 1

    elif inputan_pengguna == "gunting" and pilihan_komputer == "kertas":
        print("Anda Menang!")
        anda_menang += 1

    else:
        print("Anda kalah!")
        komputer_menang += 1

print("Anda menang", anda_menang, "kali.")
print("Anda Menang", komputer_menang, "kali.")
print("Sampai jumpa!\n\n")
