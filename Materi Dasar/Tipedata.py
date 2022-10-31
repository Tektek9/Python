#a=10, a adalah variabel dengan nilai a

import ctypes
from dataclasses import dataclass

_interger = 10

# perintah dibawah untuk print data dan melihat type data
# tipe data: Interger sebagai tipedata default
print("Data: ", _interger)
print("Bertipe: ", type(_interger), "\n")

# tipe data: Float untuk angka yang ada koma
data_float = 15.5
print("Data: ", data_float)
print("Bertipe: ", type(data_float), "\n")

# untuk type data doubel tidak ada

# tipe data: String (kumpulan Karakter)
data_string = "Budi Gentolet"
print("Data: ", data_string)
print("Bertipe: ", type(data_string), "\n")

# tipe data: Bolean atau true false
data_bool = True
print("Data: ", data_bool)
print("Bertipe: ", type(data_bool), "\n")

# tipe data kompleks
data_kompleks = complex(9,7)
print("Data: ", data_kompleks)
print("Bertipe: ", type(data_kompleks))

# tipe data double dari bahasa C
from ctypes import c_double
data_c_double = c_double(9.5)
print("Data: ", data_c_double)
print("Bertipe: ", type(data_c_double))