drinks = { "Klaus": "Bier",
           "Peter": "Wein",
           "Matthias": "Spritzwein",
           "Katharina": "Cider"}

name = input("Name: ")

if name not in drinks:
    print("unbekannter Name", name)

else:
    print("Lieblingsgetränk von", name, "ist", drinks[name])