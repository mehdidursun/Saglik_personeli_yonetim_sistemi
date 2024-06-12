class Hasta:
    def __init__(self, hasta_no, isim, soyisim, dogum_tarihi, hastalik, tedavi):
        self.__hasta_no = hasta_no
        self.__isim = isim
        self.__soyisim = soyisim
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi

    @property
    def hasta_no(self):
        return self.__hasta_no

    @property
    def isim(self):
        return self.__isim

    @isim.setter
    def isim(self, value):
        self.__isim = value

    @property
    def soyisim(self):
        return self.__soyisim

    @soyisim.setter
    def soyisim(self, value):
        self.__soyisim = value

    @property
    def dogum_tarihi(self):
        return self.__dogum_tarihi

    @dogum_tarihi.setter
    def dogum_tarihi(self, value):
        self.__dogum_tarihi = value

    @property
    def hastalik(self):
        return self.__hastalik

    @hastalik.setter
    def hastalik(self, value):
        self.__hastalik = value

    @property
    def tedavi(self):
        return self.__tedavi

    @tedavi.setter
    def tedavi(self, value):
        self.__tedavi = value

    def tedavi_suresi_hesapla(self):
        #  tedavi süresi,hastalığın karakter sayısının 5 fazlası olsun.
        return len(self.__hastalik) +5  

    def __str__(self):
        return f"Hasta No: {self.__hasta_no}, İsim: {self.__isim}, Soyisim: {self.__soyisim}, Doğum Tarihi: {self.__dogum_tarihi}, Hastalık: {self.__hastalik}, Tedavi: {self.__tedavi}, Tedavi Süresi: {self.tedavi_suresi_hesapla()} gün"

