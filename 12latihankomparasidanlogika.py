#MEMBUAT LATIHAN OPERASI LOGIKA DAN KOMPARASI
#---3+++10---
Data = float(input("Masukkan angka yang\nlebih dari 3\natau\nkurang dari 10 :"))
lebihdari3 = Data > 3
kurangdari10 = Data < 10
print("angka lebih dari 3 =",lebihdari3)
print("angka kurang dari 10 =",kurangdari10)
keduanya = lebihdari3 and kurangdari10
print("angka memenuhi keduanya =",keduanya)

#+++4---8+++12---
Data = float(input("Masukkan angka yang\nkurang dari 4\natau\ndiantara 8 dan 12 :"))
kurangdari4 = Data < 4
lebihdari8 = Data > 8
kurangdari12 = Data < 12
leb8kur12 = lebihdari8 and kurangdari12
kur4atleb8kur12 = leb8kur12 or kurangdari4
print("angka kurang dari 4 =",kurangdari4)
print("angka diantara 8 dan 12 =",leb8kur12)
print("angka kurang dari 4\natau diantara 8 dan 12 =",kur4atleb8kur12)