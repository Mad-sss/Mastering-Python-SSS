#latihan konversi satuan tempeature

#program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukkan suhu dalam celcius : '))
print("suhu adalah",celcius, "celcius")

#reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah", reamur, "reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah", fahrenheit,"fahrenheit")

#Kelvin
Kelvin = celcius + 273
print("suhu dalam kelvin adalah",Kelvin,"kelvin")