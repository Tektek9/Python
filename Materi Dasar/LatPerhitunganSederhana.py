#Program latihan soal
from cgi import print_arguments


print("PROGRAM KONVERSI TEMPERATUR")

#Celcius
celcius = float(input("Masukan suhu dalam Celcius: "))
print ("Suhu: ",celcius,"Celcius")

#Reamur
reamur = (4/5)*celcius
print("      ",reamur,"Reamur")

#Fahrenheit
fahrenheit = ((9/4)*reamur)+32
print("      ",fahrenheit,"Fahrenheit")

#Kelvin
kelvin = celcius+273.15
print("      ",kelvin,"Kelvin")

#Fahrenheit ke Kelvin
C1 = ((celcius-32)*(5/9))+273.15
print("Konversi Fahrenheit ke Kelvin:",C1,"Kelvin")

#Kelvin ke Fahrenheit
C2 = ((9/5)*(celcius-273.15))+32
print("Konversi Kelvin: ke Fahrenheit:",C2,"Fahrenheit")