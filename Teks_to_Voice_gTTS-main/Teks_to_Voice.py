from gtts import gTTS
 
isi = "Isikan teks yang nantinya akan dibuat sebagai suara"
voice = gTTS(text=isi, lang="id")  
voice.save("Suaraku.mp3")
print("Suskes membuat suara")

#isi2 = "Semua pintu terbuka mohon untuk segera diamankan"
#voice2 = gTTS(text=isi2, lang="id")
#voice2.save("semua.mp3")
#print("Sukses muat semua")
#by Taukhid Aji N