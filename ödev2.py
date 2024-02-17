
ogrenciler=["Gonca Demirci","Emir Asaf","Adem Demirci"]

# Aldığı isim soy isim ile listeye öğrenci ekleyen
def ogrenciEkle():
    isim=input("Öğrenci İsmini giriniz:")
    soyİsim=input("Öğrenci soyadını giriniz:")
    ogrenci = isim + " " + soyİsim
    ogrenciler.append(ogrenci)
    print("Öğrenci listeye eklenmiştir")

ogrenciEkle()
print(ogrenciler)

# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
def ogrenciSil():
    isim = input("Öğrenci ismini giriniz: ")
    soyisim = input("Öğrenci soyismini giriniz: ")
    ogrenci = isim + " " + soyisim
    if ogrenci in ogrenciler:
        ogrenciler.remove(ogrenci)
        print("Öğrenci listeden silinmiştir.")
    else:
        print("Öğrenci bulunamadı.")

ogrenciSil()
print(ogrenciler)


# Listeye birden fazla öğrenci eklemeyi mümkün kılan
def ogrenciCokluEkle():
    adet=int(input("eklenecek öğrenci sayısını giriniz"))
    for i in range(adet):
        isim = input("Öğrenci ismini giriniz: ")
        soyisim = input("Öğrenci soyismini giriniz: ")
        ogrenci = isim + " " + soyisim
        ogrenciler.append(ogrenci)
       
    print(f"{adet} öğrenci listeye eklenmiştir", ogrenciler)
ogrenciCokluEkle()   


# Listedeki tüm öğrencileri tek tek ekrana yazdıran
ogrenciler=["Gonca Demirci","Emir Asaf","Adem Demirci"]
def ogrencileriListele():
     for ogrenci in ogrenciler:
        print(ogrenci)
ogrencileriListele()

# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
for i in range (len(ogrenciler)):
    print(f"{i+1}. Öğrenci : {ogrenciler[i]}")

# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)       
def ogrenci_coklu_sil():
    while True:
        silinecek_isimler = input("Silinecek öğrenci isimlerini ve soyisimlerini  virgülle ayırarak giriniz (Çıkmak için 'q' tuşuna basın): ").split(",")
        if silinecek_isimler[0].lower() == 'q':
            break  # q tuşuna basıldığında döngüyü sonlandır
        silinecek_sayisi = 0
        for isim in silinecek_isimler:
            if isim.strip() in ogrenciler:
                ogrenciler.remove(isim.strip())
                silinecek_sayisi += 1
        print(f"{silinecek_sayisi} öğrenci başarıyla silindi.")

ogrenci_coklu_sil()
        


