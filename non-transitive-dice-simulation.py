import random as r
import time as t
import matplotlib.pyplot as plt

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
        self.stats = {}
        
    def würfeln(self, würfe: int, zweiter_wurf: bool):
        for _ in range(0, würfe):
            erster_wurf = r.choice(self.würfel)
            if zweiter_wurf == True:
                erster_wurf = erster_wurf + r.choice(self.würfel)
            self.ergebnisse.append(erster_wurf)

    def statistik(self):
        for i in list(set(self.ergebnisse)):
            self.stats[i] = self.ergebnisse.count(i)
        bars = plt.bar(self.stats.keys(), self.stats.values())

        for bar in bars:
            height = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                height,
                str(height),
                ha='center', va='bottom'
            )

        plt.xlabel("Zahl")
        plt.ylabel("Anzahl")
        plt.title(self.name)
        plt.show()

spieler1 = Spieler(name = "1")
spieler2 = Spieler(name = "2")

würfe = int(input("\nWie oft soll gewürfelt werden?\n $ "))
zweiter_wurf = input("\nSollen die beiden Spieler mit zwei Würfeln spielen? [y/N]\n$ ")
if zweiter_wurf == "y":
    starttime = t.time()
    spieler1.würfeln(würfe = würfe, zweiter_wurf = True)
    spieler2.würfeln(würfe = würfe, zweiter_wurf = True)
else:
    starttime = t.time()
    spieler1.würfeln(würfe = würfe, zweiter_wurf = False)
    spieler2.würfeln(würfe = würfe, zweiter_wurf = False)

for i in range(0, len(spieler1.ergebnisse) - 1):
    if spieler1.ergebnisse[i] > spieler2.ergebnisse[i]:
        spieler1.win_count = spieler1.win_count + 1
    elif spieler1.ergebnisse[i] < spieler2.ergebnisse[i]:
        spieler2.win_count = spieler2.win_count + 1

endtime = t.time()
input(f"\nDas Würfeln dauerte {endtime - starttime} Sekunden...")

input(f"Von {würfe} Würfeln hatte Spieler {spieler1.name} {spieler1.win_count}-mal die höher Zahl gewürfelt und der Spieler {spieler2.name} {spieler2.win_count}-mal...")
input(f"Gewinnchance Spieler {spieler1.name} mit Würfel {spieler1.würfel}: {spieler1.win_count / würfe * 100}%\nGewinnchance Spieler {spieler2.name} mit Würfel {spieler2.würfel}: {spieler2.win_count / würfe * 100}%\n")

spieler1.statistik()
input()
spieler2.statistik()
input()
