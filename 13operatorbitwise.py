print("========OR========")
a = 9
b = 5
print("nilai : ",a," , binary : ",format(a,'08b'))
print("nilai : ",b," , binary : ",format(b,'08b'))
print("--------------------(|)")
print("nilai : ",a|b," , binary : ", format(a|b,'08b'))


print("========AND========")
a = 9
b = 5
print("nilai : ",a," , binary : ",format(a,'08b'))
print("nilai : ",b," , binary : ",format(b,'08b'))
print("--------------------(&)")
print("nilai : ",a&b," , binary : ", format(a&b,'08b'))


print("========XOR========")
a = 9
b = 5
print("nilai : ",a," , binary : ",format(a,'08b'))
print("nilai : ",b," , binary : ",format(b,'08b'))
print("--------------------(^)")
print("nilai : ",a^b," , binary : ", format(a^b,'08b'))


print("========NOT========")
a = 9
b = 5
c = ~a
print("nilai : ",a," , binary : ",format(a,'08b'))
print("nilai : ",b," , binary : ",format(b,'08b'))
print("--------------------(~)")
print("nilai : ",c," , binary : ",format(c,'08b'))
d = 0b0000001001
e = 0b1111111111
print('nilai : ',e^d,' , binary : ',format(e^d,'08b'))


print("========SHIFT RIGHT>>========")
a = 9
b = 5
c = a >> 2
print("nilai : ",a," , binary : ",format(a,'08b'))
print("nilai : ",b," , binary : ",format(b,'08b'))
print("--------------------(~)")
print("nilai : ",c," , binary : ",format(c,'08b'))


print("========SHIFT LEFT>>========")
a = 9
b = 5
c = a << 2
print("nilai : ",a," , binary : ",format(a,'08b'))
print("nilai : ",b," , binary : ",format(b,'08b'))
print("--------------------(~)")
print("nilai : ",c," , binary : ",format(c,'08b'))