print("Selamat Datang, di quiz pancasila")

bermain = input("apakah kamu mau bermain?")
if bermain.lower() != "ya":
    quit()

print("ok! Mari kita bermain :)")
skor = 0
jawab = input("Apa bunyi sila pertama pancasila?")
if jawab.lower() == "ketuhanan yang maha esa":
    print("Benar!")
    skor += 1
else:
    print("salah!")

jawab = input("Apa bunyi sila kedua pancasila?")
if jawab.lower() == "kemanusiaan yang adil dan beradab":
    print("Benar!")
    skor += 1
else:
    print("salah!")

jawab = input("Apa bunyi sila ketiga pancasila?")
if jawab.lower() == "persatuan indonesia":
    print("Benar!")
    skor += 1
else:
    print("salah!")

jawab = input("Apa bunyi sila keempat pancasila?")
if jawab.lower() == "kerakyatan yang di pimpin oleh hikmat kebijaksanaan dalam permusyawaratan perwakilan":
    print("Benar!")
    skor += 1
else:
    print("salah!")

jawab = input("Apa bunyi sila kelima pancasila?")
if jawab.lower() == "keadilan sosial bagi seluruh rakyat indonesia":
    print("Benar!")
    skor += 1
else:
    print("salah!")

print("kamu mendapatkan " + str(skor) + " jawaban benar!")
print("kamu mendapatkan " + str((skor/5) * 100) + " %.!")
