27
x=input("Lütfen Doğum Gününüzü GG-AA-YYYY şeklinde giriniz  :")
y=x.split("-")
Aylar=("-","Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık")
print("Siz "+ Aylar[int(y[1])]+" ayında doğdunuz")
