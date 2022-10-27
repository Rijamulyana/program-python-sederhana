from gtts import gTTS
import os

tulis = open("tes.txt")
buka = tulis.read()
bahasa = 'en'

bicara = gTTS(text=buka, slow=False)

bicara.save("bicara.wav")
os.system("bicara.wav")
