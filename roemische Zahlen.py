'''
Aufgabe: Schreiben Sie ein Python-Programm, das eine beliebige römische Zahl in eine
         „gewöhnliche” Dezimalzahl umrechnet.
'''
# Erstelle ein Dictionary, "übersetze" römische Zahlen in Dezimalzahlen
roemische_zahlen = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
# Instanziiere eine Variable mit dem Namen "dezimal_zahlen"
dezimal_zahlen = 0

# User Input wird in input_roemisch "gespeichert"
if __name__ == "__main__":
    input_roemisch = input("Römische Zahl eingeben: ") 

# Instanziiere eine Variable mit dem Namen "vorherige_zahl"
vorherige_zahl = 0

# In Python ist es möglich, über einen String zu iterieren... Iteriere mit einer for-Schleife
for char in input_roemisch:
        # Wenn die nachfolgende Ziffer/Zahl größer ist als die vorherige Ziffer/Zahl...
        if roemische_zahlen[char] > vorherige_zahl:
            # Subtrahiere die vorherige Zahl von der nachfolgenden Zahl
            dezimal_zahlen -= vorherige_zahl
        # Wenn die nachfolgende Ziffer/Zahl kleiner oder gleich groß ist wie die vorherige Ziffer/Zahl...
        else:
            # Addiere die vorherige Zahl mit der nachfolgenden Zahl
            dezimal_zahlen += vorherige_zahl
            # Übersetze die vorherige römische Zahl in eine Dezimalzahl
        vorherige_zahl = roemische_zahlen[char]
        # Addiere die vorherige Zahl zur Dezimalzahl
dezimal_zahlen += vorherige_zahl 

print("Als Dezimalzahl: " + str(dezimal_zahlen)) # Ausgabe der Dezimalzahl