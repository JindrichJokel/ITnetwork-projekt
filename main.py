from evidence import Evidence

print('______________________')
print('Evidence pojistencu')
print('______________________')
pojistenci = []

evidence = Evidence()
while True:
   
    klavesa = int(input('vyber cislo '))
    
    if klavesa == 2:
        evidence.hledej()

    if klavesa==5:
        evidence.vypis()
        

        
    if klavesa == 1:
        evidence.pridat()
        

print("konec smicky")



