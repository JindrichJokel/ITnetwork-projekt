class Pojistenec:
    def __init__(self,jmeno,prijmeni,telefon,vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.telefon = telefon
        self.vek = vek
    def __str__(self):
        return f'Jmeno: {self.jmeno}, prijmeni: {self.prijmeni}, telefon: {self.telefon}, vek: {self.vek}'
