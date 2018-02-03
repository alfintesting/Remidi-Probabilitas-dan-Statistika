#!/usr/bin/python
import math

print("Nama\t\t:Alfin Maghfiroh")
print("Nim\t\t:A11.2016.09542")
print("Kelompok\t:A11.4301")
print("Matkul\t\t:Probabilitas dan Statistika ")

print("\n\n\t\t\t\tSoal no 2 :\n")
print("Seratus orang mengalami obesitas di ukur berat badannya untuk sebuah penelitian.")
print("Diketahui rata-rata dari pengukuran berat badan tersebut adalah 85.800 g dengan")
print("simpangan baku 0,15 kg. Tentukan rata - rata sesungguhnya dengan menggunakan ")
print("interval kepercayaan 95% !\n\n")

print("Diketahui :")
n = 100
x = 85800/1000
a = 0.15
b = 95/100
b = 1.96
print("n = ",n)
print("x = ",x,"kg")
print("a = ",a)
print("b= ",b)


print("\nDitanya : rata rata sesungguhnya (y) \n")

print("Jawab :")
print("y = x -+ b  / (a/akar(n))")
print("y = ",x,"-+",b,"(",a,"/","akar(",n,"))")
c = b*(a/math.sqrt(100))
print("y = ",x,"-+",c)
kurang = x-c
lebih = x+c
print("y = ",kurang," < y < ",lebih)


print("\n\n===========================================")
print("\nketerangan : ")
print("y = rata -rata sesungguhnya (yang dicari)")
print("x = rata - rata")
print("a = simpangan baku")
print("b = interval Kepercayaan ")
print("n = jumlah sample ")




