#kita belajar casting
#merubah dari sat tipe ke tipe lain
#tipe data = int, float, str, bool


##INTEGER
print("===INTEGER===")
data_int = 9;
print("data = ", data_int, ", type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai int=0
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_bool, ",type =", type(data_bool))


##FLOAT
print("===FLOAT===")
data_float = 9.9;
print("data = ", data_float, ", type =", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) #akan false jika nilai int=0
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_bool, ",type =", type(data_bool))


##BOOLEAN
print("===BOOLEAN===")
data_bool = True;
print("data = ", data_bool, ", type =", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool) #akan false jika nilai int=0
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_float, ",type =", type(data_float))


##STRING
print("===STRING===")
data_string = "10";
print("data = ", data_string, ", type =", type(data_string))

data_int = int(data_string)
data_bool = bool(data_string)
data_float = float(data_string) #akan false jika nilai int=0
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_bool, ",type =", type(data_bool))
print("data = ", data_float, ",type =", type(data_float))
