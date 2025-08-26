import random as r
import time as t

class Spieler:
    def __init__(self, name: str):
        self.name = name

        self.würfel = input(f"\nMit welchen Würfel soll Spieler {self.name} würfeln?\nroter Würfel [4,4,4,4,4,9]\ngrüner Würfel [0,5,5,5,5,5]\nblauer Würfel [2,2,2,7,7,7]\npinker Würfel [1,1,6,6,6,6]\ngelber Würfel [3,3,3,3,7,7]?\nr = roter Würfel, gr = grüner Würfel, b = blauer Würfel, ge = gelber Würfel, p = pinker Würfel\n $ ")
        if self.würfel == "r":
            self.würfel = [4,4,4,4,4,9]
        elif self.würfel == "gr":
            self.würfel = [0,5,5,5,5,5]
        elif self.würfel == "b":
            self.würfel = [2,2,2,7,7,7]
        elif self.würfel == "ge":
            self.würfel = [3,3,3,3,7,7]
        elif self.würfel == "p":
            self.würfel = [1,1,6,6,6,6]

        self.ergebnisse = []
        self.win_count = 0
        
    def würfeln(self, würfe: int, zweiter_wurf: bool):
        for _ in range(0, würfe):
            erster_wurf = r.choice(self.würfel)
            if zweiter_wurf == True:
                erster_wurf = erster_wurf + r.choice(self.würfel)
            self.ergebnisse.append(erster_wurf)

spieler_count: int = int(input("\nWie viele Spieler sollen würfeln? [2/3]\n$ "))
spieler_liste: list = []

for i in range(0, spieler_count):
    spieler_liste.append(Spieler(name = str(i + 1)))

würfe = int(input("\nWie oft soll gewürfelt werden?\n $ "))

zweiter_wurf = input("\nSollen die Spieler mit zwei Würfeln spielen? [y/N]\n$ ")
   
if zweiter_wurf == "y":
    starttime = t.time()
    for spieler in spieler_liste:
        spieler.würfeln(würfe = würfe, zweiter_wurf = True)
else:
    starttime = t.time()
    for spieler in spieler_liste:
        spieler.würfeln(würfe = würfe, zweiter_wurf = False)

for i in range(0, len(spieler_liste[0].ergebnisse)):
    vergleich = []
    for spieler in spieler_liste:
        vergleich.append(spieler.ergebnisse[i])
    spieler_liste[vergleich.index(max(vergleich))].win_count = spieler_liste[vergleich.index(max(vergleich))].win_count + 1

endtime = t.time()
input(f"\nDas Würfeln dauerte {endtime - starttime} Sekunden...")

for spieler in spieler_liste:
    input(f"\nDer Spieler {spieler.name} mit dem Würfel {spieler.würfel} gewann {spieler.win_count} von {würfe} Würfen und hat somit eine Gewinnchance von {spieler.win_count / würfe * 100}% ...")

input("\nEXIT\n\n")
