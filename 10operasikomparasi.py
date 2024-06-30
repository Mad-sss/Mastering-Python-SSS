#Operasinya ada >,<,>=,<=,==,!=,is,is not
#hasilnya selalu boolean
#b=4 <----- masuk ke dalam memory dan termasuk object
#5/3/4/6/2/1/754/99 adalah literal
#>,<,>=,<=,==, dan != untuk membandingkan object dan literal
#is,is not untuk membandingkan object saja
print("\nOPERASI PERBANDINGAN\n")
w = 1
x = 3
y = 7
z = 1

hasil1 = x>y
hasil2 = x<z
hasil3 = x==3
hasil4 = y<=7
hasil5 = y>=8
hasil6 = y!=7
hasil7 = z is w
hasil8 = z is not w
print(hasil1)
print(hasil2)
print(hasil3)
print(hasil4)
print(hasil5)
print(hasil6)
print(hasil7)
print(hasil8)
print("id z",hex(id(z)))
print("id w",hex(id(w)))