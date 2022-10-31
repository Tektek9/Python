#Tujuannya diadakan OOP adalah untuk mempermudah object untuk lebih mudah diakses di class lain

class Hero: #template
    pass 

hero1 = Hero() #object / instance (instanslate)
hero2 = Hero()
hero3 = Hero()

hero1jamban = "Jambanmu" #cara print perintah diambil sama dengan "hero1.name"
hero1.name = "Yakjuj" #name adalah atribut dari template Hero()
hero1.health = 10000 #health adalah atribut dari template Hero()

hero2.name = "Makjuj"
hero2.health = 100

hero3.name = "AAKKUU"
hero3.health = 1000

print(hero1) #print object dari "class Hero:" dan print memory addressnya
print(hero1.__dict__) #print atribut
print(hero1.name) #print objek
print(hero1jamban) #nama yang dipanggil sama dengan nama oop prosedural sama saja dengan pemanggilan biasa

#ketika menggunakan perintah dibawah akan lebih sulit implementasinya ketika ingin diakses diberbagai macam kelas
Pahlawannama = "Budi"
Pahlawankekuatan = 900
Pahlawannyawa = 9000