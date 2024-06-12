from Personel import Personel

class Hemsire(Personel):
    def __init__(self, personel_numarasi, isim, soyisim, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_numarasi, isim, soyisim, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    @property
    def calisma_saati(self):
        return self.__calisma_saati

    @calisma_saati.setter
    def calisma_saati(self, value):
        self.__calisma_saati = value

    @property
    def sertifika(self):
        return self.__sertifika

    @sertifika.setter
    def sertifika(self, value):
        self.__sertifika = value

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
        return f"{super().__str__()}, Çalışma Saati: {self.calisma_saati}, Sertifika: {self.sertifika}, Hastane: {self.hastane}"



