# Belajar Aritmatika

# nilai_a = input("Masukan Nilai A: ")
# nilai_b = input("Masukan Nilai B: ")
# a = int(nilai_a)#Untuk Pemakaian Variabel Inputan wajib diparsing terlebih dahulu 
# b = int(nilai_b)#Untuk Pemakaian Variabel Inputan wajib diparsing terlebih dahulu 
# hasli2 = a-b #Pengurangan°
# hasil1 = a+b #Penjumlahan
# hasil3 = a/b #Pembagian
# hasil4 =  a*b #Perkalian
# hasil5 = a**b #Pangkat atau Eksponen
# hasil6 = a%b #Modulus atau sisa hasil bagi
# hasil7 = a//b #Floor division pembagian yang dibagi lagi atau dibulatkan belakangnya
# print(a,'+',b,'=',hasil1)
# print(a,'-',b,'=',hasli2)
# print(a,'/',b,'=',hasil3)
# print(a,'*',b,'=',hasil4)
# print(a,'pangkat',b,'=',hasil5)
# print(a,'modulus',b,'=',hasil6)
# print(a,"//",b,'=',hasil7)
# print("tipe data a:",type(a))
# print("tipe data b:",type(b ))

x = 3
y = 2
z = 4

hasilku = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasilku)

"""
    Urutan Pengerjaan yang dikerjakan terlebih dahulu 
    1. Yang Dikurung ()
    2. Exponen atau Pangkat **
    3. Perkalian * atau Pembagian /
    4. Penjumlahan + atau Pengurangan -
"""