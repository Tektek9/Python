#Input Data User

data = input("Masukan Data: ") #APABILA DIISI BUKAN ANGKA AKAN ERROR KARENA ADA FLOAT
angka = float(data) #String ke Float
huruf = int(angka) #Float ke Int
bolean = bool(huruf) #Int ke Boolean
print("Data 1:",data)  
print("Bertipe: ", type(data))
print("Data 2:",angka)#Float selain angka tidak bisa diprint
print("Bertipe: ", type(angka))
print("Data 3:",huruf)#Int bisa diisi angka dan huruf
print("Bertipe: ", type(huruf))
print("Data 4:",bolean)#Apabila data berisi 0 maka printoutnya False
print("Bertipe: ", type(bolean))

#khusus Boolean data wajib dijadikan INT dulu lalu di parsing ke BOOL
data_boolean = bool(input("Masukan Nilai Boolean:"))
print("Data: ", data_boolean)
print("Bertipe:", type(data_boolean))