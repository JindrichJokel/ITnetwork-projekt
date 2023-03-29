import os

class Print:
    def clear(self):
        clear = clear = lambda: os.system('cls')
        input("pokracujte libovolnou klavesnici ...")
        clear()


    
    def vypis(self):
        print('______________________')
        print('Evidence pojistencu')
        print('______________________')
        print('')
        print('Vyberte akci:')
        print('1 - Pridat noveho pojistneho')
        print('2 - Vypsat vsechny pojistne uzivatele')
        print('3 - Vyhledat pojistneho')
        print('4 - Smazat pojistneho')        
        print('5 - Ukoncit program')
    
    def konec(self):

        print('______________________')
        print('Ukonceni programu Evidence')
        print('______________________')