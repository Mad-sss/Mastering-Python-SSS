#operasi yang dapat dilakukan dengan peningkatan
#operasi ditambah dengan assignment

a = 5 # adalah assignment
print("nilai a = ",a)

a += 1 #artinya adalah a = a + 1
print('nilai a += 1, nilai a menjadi ',a)

a -= 2 #artinya adalah a = a - 1
print('nilai a -= 2, nilai a menjadi ',a)

a *= 5 #artinya adalah a = a * 1
print('nilai a *= 5, nilai a menjadi ',a)

a /= 2 #artinya adalah a = a / 1
print('nilai a /= 2, nilai a menjadi ',a)

b = 10
print('\nnilai b = ',b)

b %= 3
print('\nnilai b %= 3 nilai b menjadi',b)

b = 10
print('\nnilai b =',b)

b //= 3
print('\nnilai b //= 3 nilai b menjadi ',b)

a = 5 
print("nilai a =",a)

a **= 3 
print("nilai a **= 3 ,nilai a menjadi",a)

c = True
print('\nnilai c =',c)

c |= True
print('nilai c |= false, nilai c menjadi',c)

c = False
print('nilai c =',c)

c |= False
print('nilai c |= False, nilai c menjadi',c)

c = True
print('nilai c %=',c)

c &= False
print('nilai c &= false, nilai c menjadi',c)

c = True
print('nilai c =',c)

c &= True
print('nilai c &= True, nilai c menjadi',c)

c = True
print('nilai c =',c)

c ^= False
print('nilai c ^= false, nilai c menjadi',c)

c = True
print('nilai c =',c)

c |= True
print('nilai c |= True, nilai c menjadi',c)

d = 0b0100
print('\nnilai d =',format(d,'04b'))
d >>= 2
print('\nnilai d >>= 2 adalah',format(d,'04b'))
d <<= 1
print('\nnilai d <<= 2 adalah',format(d,'04b'))