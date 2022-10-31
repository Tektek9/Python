#Tujuannya diadakan OOP adalah untuk mempermudah object untuk lebih mudah diakses di class lain

# class Hero: #template
#     def __init__(self): #self adalah hero1
#         #__init__ akan dieksekusi pertamakali si object dibuat 
#         print("hallo")
        
        
        
        
# hero1 = Hero() #Ketika dijalankan OBJECT akan memanggil def __init__(self): print("hallo")

from cgi import print_arguments


class Hero1: #template
    def __init__(self,inputName): #inputName adalah argumen yang nantinya akan dipakai untuk menampung nilai dari "self.name"
        self.name = inputName
        # print("hallo", inputName) #output "hallo 10"
                
hero1 = Hero1(10) #Ketika dijalankan OBJECT akan memanggil def __init__(self):  print("hallo")


class Hero2: #template
    
    jumlah = 0
    
    def __init__(self,inputName, inputPower, inputArmor): #inputName adalah argumen yang nantinya akan dipakai untuk menampung nilai dari "self.name"
        self.name = inputName
        self.power = inputPower
        self.armor = inputArmor
        Hero2.jumlah += 1
        print("membuat Hero dengan nama"+inputName)
        
hero2 = Hero2("Yakjuj", 1000, 90)
# print(Hero2.jumlah)
hero3 = Hero2("Makjuj", 990, 95)
# print(Hero2.jumlah)
hero4 = Hero2("Pocong", 15, 10)
# print(Hero2.jumlah)

# print("Nama Hero: ",hero2.name) #printout Nama Hero2 Yakjuj
# print("Armor Hero Makjuj: ",hero3.armor) #printout Armor Hero3 990
# print("Power Hero Pocong: ",hero4.power) #printout Power Hero4 10
# print(hero2.__dict__) #printout atribut Hero Yakjuj
# print(Hero2.jumlah)
# print(hero3.__dict__)
# print(Hero2.jumlah)
# print(hero4.__dict__)
# print(Hero2.jumlah)
# print(Hero2.__dict__) #printout attribut Hero2