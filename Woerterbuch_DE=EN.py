#Aufgabe: Wörterbuch DE -> EN
#Eingabe Deutscher Begriff und ausgabe des englischen wortes,
#wenn Wort nicht in Wörterbuch --> entsprechende Ausgabe

woerterbuch = {"apfel":"apple",
               "birne":"pear",
               "kirsche":"cherry",
               "melone":"melon",
               "marille":"apricot",
               "pfirsich":"peach"}   


eingabe = input("Eingabe des deutschen Wortes:  ")
eingabe = eingabe.lower()


if eingabe not in woerterbuch:
    print("Wort nicht gefunden")
    
else:
    print("Übersetzung Englisch:   ", woerterbuch[eingabe])