#Logika Komparasi
#Khusus untuk inputan berupa angka bisa menggunakan Float atau Int

#IRISAN
inputUser = float(input("Silahkan masukan angka yang bernilai kurang dari 3 atau lebih dari 10: \n"))

#Memeriksa angka yang kurangdari 3 
isKurangDari = (inputUser < 3)
print ("Nilai kurang dari 3: ",isKurangDari)

#Memeriksa angka yang lebihdari 10
isLebihDari = (inputUser > 10)
print ("Nilai lebih dari 10: ",isLebihDari) 

#Memeriksa apakah angka diluar range 3 - 10
isCorrect = isKurangDari or isLebihDari
print ("Nilai diluar range 3-10: " , isCorrect)

#GABUNGAN
inputUser = float(input("Silahkan masukan angka yang bernilai lebih dari 3 atau kurang dari 10: \n"))

#Memeriksa angka yang lebih dari 3
isLebihDari = (inputUser > 3)
print ("Nilai lebih dari 3: ",isLebihDari) 

#Memeriksa angka yang kurang dari 10
isKurangDari = (inputUser < 10)
print ("Nilai kurang dari 10: ",isKurangDari) 

#Memeriksa apakah angka dirange 3 - 10
isCorrect = isKurangDari and isLebihDari 
print ("Nilai dirange 3-10: " , isCorrect)