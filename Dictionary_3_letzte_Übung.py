#Woeterbuch 

wb = {"Bier":"Beer",
      "Wein":"Wine",
      "Cocktail":"Cocktail",
      "Wasser":"Water",
      "Saft":"Juice",
      "Kaffee":"Coffee"}

print("Willkommen im Getränke-Wörterbuch, wählen Sie eine Funktion:")
print("Wähle [T] um Getränke auf Englisch zu übersetzen")
print("Wähle [New] um eine Übersetzung eines Getränks einzuspeichern")
    

    
correct = False
    
while correct == False:        
    eing = input("Wähle eine Funktion mittels Eingabe: ")    
    
    if eing == "T":
        word=input("Bitte geben Sie den deutschen Getränkenamen ein: ") 
        if word in wb:
            print("Übersetzung ins Englische: ",wb[word]) 
        else:
            print('nicht in Datenbank')
    elif eing == "New":
        wb[input('deutscher Begriff:')] = input('englischer Begriff:') 
        
        
    else:
        print("Unknown answer")
