class Personel:
    def __init__(self, personel_numarasi, isim, soyisim, departman, maas):
        self.__personel_numarasi = personel_numarasi
        self.__isim = isim
        self.__soyisim = soyisim
        self.__departman = departman
        self.__maas = maas

    # Tek bir metodda property ve setter fonksiyonları
    @property
    def personel_numarasi(self):
        return self.__personel_numarasi

    @property
    def isim(self):
        return self.__isim

    @property
    def soyisim(self):
        return self.__soyisim

    @property
    def departman(self):
        return self.__departman

    @property
    def maas(self):
        return self.__maas

    @maas.setter
    def maas(self, deger):
        self.__maas = deger

    def get_info(self):
        return {
            "personel_numarasi": self.personel_numarasi,
            "isim": self.isim,
            "soyisim": self.soyisim,
            "departman": self.departman,
            "maas": self.maas
        }

    def __str__(self):
        return f"Personel Numarası: {self.personel_numarasi}, İsim: {self.isim}, Soyisim: {self.soyisim}, Departman: {self.departman}, Maas: {self.maas}"
