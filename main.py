from evidence import Evidence
from print import Print

pojistenci = []
evidence = Evidence()
printer = Print()
while True:
    
    printer.vypis()
    klavesa = int(input(''))

    if klavesa == 1:
        evidence.pridat()
        printer.clear()
    if klavesa == 2:
        evidence.vypis()
        printer.clear()

    if klavesa == 3:
        evidence.hledej()
        printer.clear()
          
    if klavesa == 4:
        evidence.smazat()
        printer.clear()


    if klavesa == 5:
        evidence.konec()
        break

        



