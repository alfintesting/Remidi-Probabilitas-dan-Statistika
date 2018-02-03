print("Nama\t\t:Alfin Maghfiroh")
print("Nim\t\t:A11.2016.09542")
print("Kelompok\t:A11.4301")
print("Matkul\t\t:Probabilitas dan Statistika ")

#!/usr/bin/python
import math

print("\n\n\t\t\t\tSoal no 1 :\n")
print("Sebuah lembaga survey melakukan kegiatan pengambilan sampel acak dari")
print("dua kelurahan tentang ketertarikan masyarakat terhadap film yang sedang")
print("digemari pekan ini. Diketahui hasil pengambilan data adalah 95 dari 300")
print("masyarakat kelurahan A dan 175 dari 280 masyarakat kelurahan B menyukai")
print("film Ayat - Ayat Cinta 2.Dengan menggunakan taraf signifikasi 0.05,uji")
print("bahwa tidak ada perbedaan proporsi populasi tersebut !\n\n")

print("Diketahui :")
x1=95
x2=175
n1=300
n2=280
P=(x1+x2)/(n1+n2)
Q=1-P

print("x1 =",x1)
print("x2 =",x2)
print("n1 =",n1)
print("n2 =",n2,"\n")

print("Ditanyakan : Z = ?\n")

print("Jawab :")
a = (x1/n1)-(x2/n2)
b= (1/n1)+(1/n2)
c = P*Q*b
d= math.sqrt(c)
Z = a/d

print("P=(x1+x2)/(n1+n2) = (",x1,"+",x2,")","/","(",n1,"+",n2,") = ",P)
print("Q = 1 - P =",Q)
print("Z = ((x1/n1)-(x2/n2)) / akar(P*Q*{(1/n1)+(1/n2)}")
print("Z = (",x1,"/",n1,")-(",x2,"/",n2,")) / akar(",P,"*",Q,"*","{(1/",n1,")+(1/",n2,")})")
print("Z = ",a,"/ akar (",b,")")
print("Z = ",Z)
