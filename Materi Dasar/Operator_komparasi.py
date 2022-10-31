""" 
    operasi komparasi 
    setiap hasil komparasi adalah boolean
    >,<,>=,<=,==,!=,is,is not
"""

a = 6
b = 3

hasil = a > b
hasil1 = a < b
hasil2 = a >= b
hasil3 = a <= b
hasil4 = a == b
hasil5 = a != b
hasil6 = a is b
hasil7 = a is not b
print (a,">",b,"=",hasil) #Hasil TRUE karena Pernyataan A>B adalah benar
print (a,"<",b,"=",hasil1) #Hasil FALSE karena Pernyataan A<B adalah salah
print (a,">=",b,"=",hasil2) #Hasil TRUE karena Pernyataan A>=B adalah benar
print (a,"<=",b,"=",hasil3) #Hasil TRUE karena Pernyataan A<=B adalah salah
print (a,"==",b,"=",hasil4) #Hasil FALSE karena Nilai A TIDAK samadengan B
print (a,"!=",b,"=",hasil5) #Hasil BENAR karena Nilai A TIDAK samadengan B
print (a," is ",b,"=",hasil6) #Hasil FALSE karena A Bukan B
print (a,"is not",b,"=",hasil7) #Hasil BENAR karena A Bukan B