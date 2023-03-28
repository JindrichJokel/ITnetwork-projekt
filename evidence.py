from pojistenec import Pojistenec

class Evidence:
    def __init__(self):
        self.pojistenci = []

    def pridat(self):
        jmeno = input(' vlozte jmeno ')
        prijmeni = input(' vlozte prijmeni ')
        telefon = input(' vlozte telefon ')
        vek = input(' vlozte vek ')
        self.pojistenci.append(Pojistenec(jmeno,prijmeni,telefon,vek))
        print("Uzivatel pridan")

    def vypis(self):
        for pojistenec in self.pojistenci:
            print(pojistenec)

    def hledej(self):

        jmenoVyhledani = input('zadejte jmeno nebo prijmeni pro vyhledani ')

        for pojistenec in self.pojistenci:
            if jmenoVyhledani in str(pojistenec):
                print("Uzivatel nalezen!")
                print(str(pojistenec))


        

        



