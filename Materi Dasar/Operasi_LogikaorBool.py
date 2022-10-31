#Operasi Logika atau Boolean

#not, or, and, xor
from traceback import print_tb

print("========NOT=======")
a = False
b = not a
print("False Not A: ",b) #Hasilnya adalah TRUE karena A False

a = True
b = not a
print("True  Not A: ",b) #Hasilnya adalah TRUE karena A False

print("==========OR===========")
a = False
b = True
c = a or b
print("False OR True: ",c) #True Karena salahsatu dari variabel bernilai True

a = True
b = False
c = a or b
print("True OR False: ",c) #True Karena salahsatu dari variabel bernilai True
a = True
b = True
c = a or b
print("True OR True: ",c) #True Karena salahsatu dari variabel bernilai True

a = False
b = False
c = a or b
print("False OR False: ",c) #False Karena tidak ada variabel bernilai True

print("==========AND==========")
a = False
b = True
c = a and b
print("False AND True: ",c) #False Karena salahsatu dari variabel bernilai False

a = True
b = False
c = a and b
print("True AND False: ",c) #False Karena salahsatu dari variabel bernilai True

a = True
b = True
c = a and b
print("True AND True: ",c) #True Karena kedua variabel bernilai True

a = False
b = False
c = a and b
print("False AND False: ",c) #False Karena kedua variabel bernilai False

print("==========XOR==========")
a = False
b = True
c = a ^ b
print("False XOR True: ",c) #True Karena salahsatu dari variabel bernilai False

a = True
b = False
c = a ^ b
print("True XOR False: ",c) #True Karena salahsatu dari variabel bernilai True

a = True
b = True
c = a ^ b
print("True XOR True: ",c) #False Karena kedua variabel bernilai True

a = False
b = False
c = a ^ b
print("False XOR False: ",c) #False Karena kedua variabel bernilai False