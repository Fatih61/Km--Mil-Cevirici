#ver1.0
print("Km->Mil çeviriciye hos geldiniz.\n Lutfen Seciniz \n 1) Km-> Mil \n 2)Mil->Km")
ss=int(input("Seçiminizi yaziniz :"))
if(ss==1):
    sayi=int(input("Km'yi giriniz :"))
    print("Mil :"+ str(sayi/1.609344))
elif(ss==2):
    sayi=int(input("Mil'i giriniz :"))
    print("Km :"+ str(sayi*1.609344))
else:
    print("Hatalı giriş yaptınız")
