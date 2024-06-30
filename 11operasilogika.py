#Ada not,or,and, dan xor
a = True
b = not a
print("====NOT====")
print("a = ",a)
print("b = ",b)

# OR jika salah satu true maka true
print("===OR===")
a = False
b = False
c = a or b
print(a,'or', b,'=', c)
a = False
b = True
c = a or b
print(a,'or', b,'=', c)
a = True
b = False
c = a or b
print(a,'or', b,'=', c)
a = True
b = True
c = a or b
print(a,'or', b,'=', c)

# AND jika salah satu false maka false
print("===AND===")
a = False
b = False
c = a and b
print(a, 'and', b,'=', c)
a = False
b = True
c = a and b
print(a, 'and', b,'=', c)
a = True
b = False
c = a and b
print(a, 'and', b,'=', c)
a = True
b = True
c = a and b
print(a, 'and', b,'=', c)

# XOR akan true jika berbeda dan akan false jika sama
print("===XOR===")
a = False
b = False
c = a ^ b
print(a,'^', b,'=', c)
a = False
b = True
c = a ^ b
print(a,'^', b,'=', c)
a = True
b = False
c = a ^ b
print(a,'^', b,'=', c)
a = True
b = True
c = a ^ b
print(a,'^', b,'=', c)
