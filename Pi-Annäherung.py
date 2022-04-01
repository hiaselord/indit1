print("PI-Rechner\n")

strAnzahlIterrationen = input("Anzahl der Schleifenwiederholungen eingeben: ")
intAnzahlIterrationen = int(strAnzahlIterrationen)

intk=0
floatpi=0
summepi=0

while intk < intAnzahlIterrationen:
    if intk%2==0:
        floatpi=(+1)/(2*intk+1)
        
    if intk%2==1:
        floatpi=(-1)/(2*intk+1)
        
        
    summepi+=floatpi
    intk+=1
    
    print("Näherung zu PI=", 4*summepi, "nach", intk, "Iterationen")