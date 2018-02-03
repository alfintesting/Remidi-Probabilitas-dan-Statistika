print("Nama\t\t:Alfin Maghfiroh")
print("Nim\t\t:A11.2016.09542")
print("Kelompok\t:A11.4301")
print("Matkul\t\t:Probabilitas dan Statistika ")
#! /usr/bin/python
print("\n\n\t\t\t\tSoal no 3 :\n")
print("Data berikut merupakan data pertumbuhan anak di sebuah posyandu dengan umur")
print("anak dinyatakan dengan x1,berat saat lahir sebagai x2,dan panjang badan")
print("anak sebagai y.Sample yang digunakan sejumlah 9 anak secara acak.")
print("Tentukan persamaan regresinya !\n\n")
x1=[78,69,77,88,67,80,74,94,102]
x2=[2.75,2.15,4.41,5.52,3.21,4.32,2.31,4.30,3.71]
y=[57.5,52.8,61.3,67.0,53.5,62.7,56.2,68.5,69.2]
n=9
#x1y
i = 0
x1y = list()
for i in range(int(n)):x1y.append(float(x1[i]*y[i]))

#x2y
i = 0
x2y = list()
for i in range(int(n)):x2y.append(float(x2[i]*y[i]))

#x1x2
i = 0
x1x2 = list()
for i in range(int(n)):x1x2.append(float(x1[i]*x2[i]))

#x1x1
i = 0
x1x1 = list()
for i in range(int(n)):x1x1.append(float(x1[i]*x1[i]))

#x2x2
i = 0
x2x2 = list()
for i in range(int(n)):x2x2.append(float(x2[i]*x2[i]))
    
Ex1=0
Ex2=0
Ey=0
Ex1y=0
Ex2y=0
Ex1x2=0
Ex1x1=0
Ex2x2=0
Eyy=0
#Ex1
i = 0
for i in x1: Ex1 = Ex1+i

#Ex2
i = 0
for i in x2: Ex2 = Ex2+i

#Ey
i = 0
for i in y: Ey = Ey+i

#Ex1y
i = 0
for i in x1y: Ex1y = Ex1y+i

#Ex2y
i = 0
for i in x2y: Ex2y = Ex2y+i

#Ex1x2
i = 0
for i in x1x2: Ex1x2 = Ex1x2+i

#Ex1x1
i = 0
for i in x1x1: Ex1x1 = Ex1x1+i

#Ex2x2
i = 0
for i in x2x2: Ex2x2 = Ex2x2+i

print("Diketahui:\n")
print("x1 = ",x1,"-> E x1 = ",Ex1)
print("x2 = ",x2,"-> E x2 = ",Ex2)
print("y  = ",y,"-> E y = ",Ey)
print("x1*y = ",x1y,"-> E x1*y =",Ex1y)
print("x2*y = ",x2y,"-> E x2*y =",Ex2y)
print("x1*x2 = ",x1x2,"-> E x1*x2 =",Ex1x2);
print("x1*x1 = ",x1x1,"-> E x1*x2 =",Ex1x1);
print("x2*x2 = ",x2x2,"-> E x1*x2 =",Ex2x2);

print("\nDitanyakan : Y = ?\n")

print("Jawab:\n")
A = (n*Ex1y)-(Ex1*Ey)
print("A = (n*E(x1*y))-(Ex1*Ey)")
print("A =(",n,"*",Ex1y,")-(",Ex1,"*",Ey,")=",A,"\n") 

B = (n*Ex2x2)-(Ex2*Ex2)
print("B = (n*E(x2*x2))-(Ex2*Ex2)")
print("B =(",n,"*",Ex2x2,")-(",Ex2,"*",Ex2,")=",B,"\n") 

C = (n*Ex1x2)-(Ex1*Ex2)
print("C = (n*E(x1*x2))-(Ex1*Ex2)")
print("C =(",n,"*",Ex1x2,")-(",Ex1,"*",Ex2,")=",C,"\n")

D = (n*Ex2y)-(Ex2*Ey)
print("D = (n*E(x2*y))-(Ex2*Ey)")
print("D =(",n,"*",Ex2y,")-(",Ex2,"*",Ey,")=",D,"\n")

E = (n*Ex1x1)-(Ex1*Ex1)
print("E = (n*E(x1*x1))-(Ex1*Ex1)")
print("E =(",n,"*",Ex1x1,")-(",Ex1,"*",Ex1,")=",E,"\n")

F = (E*B)-(C*C)
print("F = (E*B)-(C*C)")
print("F = (",E,"*",B,")-(",C,"*",C,")=",F,"\n")

b1 = ((A*B)-(C*D))/F
print("b1 = ((A*B)-(C*D))/F")
print("b1 = ((",A,"*",B,")-(",C,"*",D,"))/",F,"=",b1,"\n")

b2 = ((D*E)-(A*C))/F
print("b2 = ((D*E)-(A*C))/F")
print("b2 = ((",D,"*",E,")-(",A,"*",C,"))/",F,"=",b2,"\n")

a = (Ey - (b1*Ex1)-(b2*Ex2))
print("a = (Ey - (b1*Ex1)-(b2*Ex2))/n")
print("a = (",Ey,"-(",b1,"*",Ex1,")-(",b2,"*",Ex2,"))/",n,"=",a,"\n")

print("Y =",a,"+",b1,"x1 +",b2,"x2")
