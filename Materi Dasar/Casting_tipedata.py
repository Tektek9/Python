# Belajar Casting
# Parsing tipedata ke tipedata yang lain
print ("==========INTERGER==========\n")
data_int = 9    
print("data: ", data_int, type(data_int),"\n")

# Parsing typedata int ke float
data_float = float(data_int)
# Parsing typedata int ke string
data_string = str(data_int)
# Parsing typedata int ke bool
data_bool = bool(data_int) #jika data_float = 0 maka output FALSE, kallau TRUE maka output data_float = 1
print("data: ", data_float, type(data_float))
print("data: ", data_string, type(data_string))
print("data: ", data_bool, type(data_bool), "\n")
print ("============================\n")


print ("============BOOL============\n")
data_bool = False    
print("data: ", data_bool, type(data_bool),"\n")


print ("==========INTERGER==========\n")
data_float = float(data_bool)
data_string = str(data_bool)
data_int = int(data_bool)
print("data: ", data_float, type(data_float))
print("data: ", data_string, type(data_string))
print("data: ", data_int, type(data_int), "\n")
print ("============================\n")


print ("============STRING===========\n")
data_string = "12"    
print("data: ", data_string, type(data_string),"\n")


print ("===========FLOAT============\n")
data_float = float(data_string)
data_int = int(data_string)
data_bool = bool(data_string)
print("data: ", data_float, type(data_float))
print("data: ", data_int, type(data_int))
print("data: ", data_bool, type(data_bool), "\n")
print ("============================")