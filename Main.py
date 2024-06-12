from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta
import pandas as pd


try:
    # Personel sınıfı için 2 nesne oluşturduk ve ekrana print ile yazdırdık
    personel1 = Personel(1900, "Ali", "Dursun", "Güvenlik", 19000)
    personel2 = Personel(1901, "Ayşe", "Dursun", "Temizlikci", 16000)
    print(personel1)
    print()
    print(personel2)
    print()

    # Doktor sınıfı için 3 nesne oluşturma ve ekrana print ile yazdırma
    doktor1 = Doktor(1902, "Ahmet", "Kirdar", "Cerrahi", 30000, "Cerrah", 10, "Akhisar Hastanesi")
    doktor2 = Doktor(1903, "Mehmet", "Karatas", "Dahiliye", 39500, "Dahiliyeci", 8, "Cigli Hastane")
    doktor3 = Doktor(1904, "Elif", "Gul", "Pediatri", 39800, "Çocuk Doktoru", 5, "Alsancak Hastanesi")
    print("*********************\n")
    print(doktor1)
    print()
    print(doktor2)
    print()
    print(doktor3)
    print()

    # Hemşire sınıfı için 3 nesne oluşturma veve ekrana print ile yazdırma
    hemsire1 = Hemsire(1905, "Zeynep", "Kaya", "Pediatri", 25000, 40, "Sertifika A", "Soma Hastanesi")
    hemsire2 = Hemsire(1906, "Fatma", "Kılıç", "Cerrahi", 25500, 45, "Sertifika B", "Esenler Hastanesi")
    hemsire3 = Hemsire(1907, "Emine", "Tas", "Dahiliye", 25200, 50, "Sertifika C", "Dumlupinar Hastane")
    print("*********************\n")
    print(hemsire1)
    print()
    print(hemsire2)
    print()
    print(hemsire3)
    print()

    # Hasta sınıfı için 3 nesne oluşturma veve ekrana print ile yazdırma
    hasta1 = Hasta(1908, "Mustafa", "Güneş", "1985-05-20", "Grip", "Dinlenme")
    hasta2 = Hasta(1909, "Merve", "Çelik", "1992-07-15", "Kırık", "Alçı")
    hasta3 = Hasta(1910, "Ahmet", "Kara", "2001-01-30", "Alerji", "İlaç Tedavisi")
    print("*********************\n")
    print(hasta1)
    print()
    print(hasta2)
    print()
    print(hasta3)
    print()
    print("*********************\n\n")

except :
    print("Hata oluştu...")


# Örnek verilerle DataFrame oluşturma işlemi
data = {
    "personel_numarasi": [1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910],
    "isim": ["Ali", "Ayşe", "Gokhan", "Anil", "Bilal", "Yildiray", "İrem", "Yilmaz", "Arda", "Hatice", "Selcuk"],
    "soyisim": ["Dursun", "Dursun", "Kirdar", "Karatas", "Gul", "Kaya", "Kılıç", "Taş", "Güneş", "Çelik", "Kara"],
    "departman": ["Yönetim", "Mühendislik", "Cerrahi", "Dahiliye", "Pediatri", "Pediatri", "Cerrahi", "Dahiliye", None, None, None],
    "maas": [19000, 16000, 30000, 39500, 39800, 25000, 25500, 25200, 0, 0, 0],
    "uzmanlik": [None, None, "Cerrah", "Dahiliyeci", "Çocuk Doktoru", None, None, None, None, None, None],
    "deneyim_yili": [None, None, 10, 8, 5, None, None, None, None, None, None],
    "hastane": [None, None, "Akhisar Hastanesi", "Cigli Hastane", "Alsancak Hastanesi", "Soma Hastanesi", "Esenler Hastanesi", "Dumlupinar Hastane", None, None, None],
    "calisma_saati": [None, None, None, None, None, 40, 45, 50, None, None, None],
    "sertifika": [None, None, None, None, None, "Sertifika A", "Sertifika B", "Sertifika C", None, None, None],
    "hasta_no": [None, None, None, None, None, None, None, None, 9, 10, 11],
    "dogum_tarihi": [None, None, None, None, None, None, None, None, "1985-05-20", "1992-07-15", "2001-01-30"],
    "hastalik": [None, None, None, None, None, None, None, None, "Grip", "Kırık", "Alerji"],
    "tedavi": [None, None, None, None, None, None, None, None, "Dinlenme", "Alçı", "İlaç Tedavisi"]
}

# DataFrame oluşturduk.
df = pd.DataFrame(data)

# fillna fonksiyonu none değerleri 0'la değiştirir.inplace=True diyerek bu değişikliğin orjinal dataframe üzerinde yapılmasını sağlarız.
df.fillna(0, inplace=True)

#uzmanlık sütununu seçer ve seçilen sütundaki benzersiz değerleri ve bu değerlerin kaç kez tekrarlandığını sayar. 
# Sonra, her bir gruptaki eleman sayısını bulmak için size() fonksiyonu kullanılır.
#reset_index() kullanarak ekranda type:int64 vs yazdırmamasını sağladık.
uzmanlik_series = df["uzmanlik"].value_counts().reset_index()
print("Uzmanlık alanlarına göre doktor sayıları:\n", uzmanlik_series)
print()

# 5 yıldan fazla deneyime sahip doktorların toplam sayısı
deneyimli_doktor_sayisi = df[(df['deneyim_yili'] > 5)].shape[0]
print("5 yıldan fazla deneyime sahip doktor sayısı:", deneyimli_doktor_sayisi)
print()

#İsim sütununa göre sort_value ile alfabetik olarak sıralar ve sorted_df değişkenine atar.
sorted_df = df.sort_values(by="isim")
print("Alfabetik olarak sıralanmış personel ve hasta bilgileri:\n", sorted_df)
print()

# Maaşı 7000 TL üzerinde olan personeller
maasi_7000_ustu = df[df['maas'] > 7000]
print("Maaşı 7000 TL üzerinde olan personeller:\n", maasi_7000_ustu)
print()

# 'dogum_tarihi' sütununu tarih-zaman nesnelerine dönüştürür 
df['dogum_tarihi'] = pd.to_datetime(df['dogum_tarihi'])

# Doğum tarihi 1990 ve sonrası olan hastalar
dogum_1990_sonrasi = df[(df['dogum_tarihi'] >= "1990-01-01")]
print("1990 ve sonrası doğumlu hastalar:\n", dogum_1990_sonrasi)
print()

# Var olan DataFrame'den yeni bir DataFrame oluşturduk.
new_df = df[['isim', 'soyisim', 'departman', 'maas', 'uzmanlik', 'deneyim_yili', 'hastane', 'dogum_tarihi', 'hastalik', 'tedavi']]
print("Yeni oluşturulan DataFrame:\n", new_df)
print()

