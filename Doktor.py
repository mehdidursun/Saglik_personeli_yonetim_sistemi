from Personel import Personel

class Doktor(Personel):
    def __init__(self, personel_numarasi, isim, soyisim, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_numarasi, isim, soyisim, departman, maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    @property
    def uzmanlik(self):
        return self.__uzmanlik

    @uzmanlik.setter
    def uzmanlik(self, value):
        self.__uzmanlik = value

    @property
    def deneyim_yili(self):
        return self.__deneyim_yili

    @deneyim_yili.setter
    def deneyim_yili(self, value):
        self.__deneyim_yili = value

    @property
    def hastane(self):
        return self.__hastane

    @hastane.setter
    def hastane(self, value):
        self.__hastane = value

    def maas_artir(self, oran):
        yeni_maas = self.maas * (1 + oran / 100)
        self.maas = yeni_maas

    def __str__(self):
        return f"{super().__str__()}, Uzmanlık: {self.uzmanlik}, Deneyim Yılı: {self.deneyim_yili}, Hastane: {self.hastane}"

