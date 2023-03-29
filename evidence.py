from pojistenec import Pojistenec

class Evidence:
    def __init__(self):
        self.pojistenci = []

    def pridat(self):
        jmeno = input(' vlozte jmeno: ')
        prijmeni = input(' vlozte prijmeni: ')
        telefon = input(' vlozte telefon: ')
        vek = input(' vlozte vek: ')
        try:
            telefon = int(telefon)
        except ValueError:
            print("")
            print("Telefon neobsahuje pouze cislo!")
        
        try:
            vek = int(vek)
        except ValueError:
            print("")
            print("Vek neobsahuje pouze cislo!")
  

        self.pojistenci.append(Pojistenec(jmeno,prijmeni,telefon,vek))
        print("")
        print("Uzivatel pridan")
        print("")
    
    def smazat(self):

        jmenoVyhledani = input('zadejte jmeno nebo prijmeni pro smazani uzivatele:')

        if not self.pojistenci:
            print("")
            print("Databaze je prazdna")
            print("")

        for pojistenec in self.pojistenci:
            if jmenoVyhledani in str(pojistenec):
                print("")
                print(f"Uzivatel {str(pojistenec)} SMAZAN!")
                print("")
                self.pojistenci.remove(pojistenec)

    def vypis(self):

        if not self.pojistenci:
            print("")
            print("Databaze je prazdna")
            print("")

            return
        print("")
        print("Vsichni uzivatele v databazi:")
        print("")
        for pojistenec in self.pojistenci:
            print(pojistenec)
        print("")

    def hledej(self):

        print("")
        jmenoVyhledani = input('zadejte jmeno nebo prijmeni pro vyhledani: ')
        if not self.pojistenci:
            print("")
            print("Databaze je prazdna")
            print("")

        for pojistenec in self.pojistenci:
            if jmenoVyhledani in str(pojistenec):
                print("")
                print("Uzivatel nalezen!")
                print(str(pojistenec))
                print("")

            if jmenoVyhledani not in str(pojistenec):
                print("")
                print("Uzivatel nenalezen")
                print("")

                

        

        



