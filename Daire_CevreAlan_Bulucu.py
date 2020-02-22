import math
print("Çember alanı ve Çevre bulucuya hoş geldiniz")
yc=float(input("Cm olarak Yaricapi giriniz :"))
s=int(input("1- Alanı bul  2-Çevreyi bul :"))
if(s==1):
    print(str(math.pi*yc**2)+" cm²")
elif(s==2) :
    print(str(2*math.pi*yc)+" cm")
else :
    print("Yanlis Giris Yaptiniz")