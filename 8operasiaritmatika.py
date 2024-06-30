#operasi aritmatika

a = 11
b = 10


#operasi penambaham
hasil = a + b
print(a, "+", b ,"=", hasil)

#operasi pengurangan
hasil = a - b
print(a, "-", b, "=", hasil)

#operasi perkalian
hasil = a * b
print(a, "x",b, "=" , hasil)

#operasi pembagian
hasil = a / b
print(a, ":", b,"=", hasil)

#operasi eksponen(pangkat)
hasil = a ** b
print(a, "pangkat", b, "=",hasil)

#operasi modulus(sisa pembagian)
hasil = a % b
print(a, "sisa pembagian",b, "=",hasil)

#operasi floot division(pembulatan pembagian)
hasil = a // b
print(a, "//",b, "=", hasil)

#prioritas operasi, operational precedence
'''
   1. ()
   2. exponen **
   3. perkalian dan teman-teman * / % //
   4. pertambahan dan pengurangan - +
'''
x = 3
y = 2
z = 4

hasil = (x + y) * z + y ** y / z % x - y
print('(',x,'+',y,') *',z,'+',y,'**',y,"/",z,"%",x,'-',y,"=", hasil)




