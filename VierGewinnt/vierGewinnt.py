#!/usr/bin/env python3
'''Vier Gewinnt!'''

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

class Spieler:
    '''Spieler Klasse'''
    def __init__(self, name: str, farbe: str) -> None:
        self.name = name
        self.farbe = farbe 
    
class Spielfeld:
    '''Spielfeld Klasse'''
    def __init__(self) -> None:
        self.breite = 7
        self.hoehe = 6
        self.spalten_stand = [0 for _ in range(self.breite)]
        self.felder = [["_" for _ in range(self.breite)] for _ in range(self.hoehe)]
        self.spielverlauf = []

    def spielfeld_anzeigen(self) -> None:
        for reihe in reversed(range(self.hoehe)):
            for spalte in range(self.breite):
                print("| " + str(self.felder[reihe][spalte]) + " ", end='')
            print("|")
        print("  0   1   2   3   4   5   6")

    def spielstein_einwerfen(self, spieler) -> bool:
        while(True):
            stelle = int(input("0 - 6: "))
            cls()
            if (self.spalten_stand[stelle] < self.hoehe):
                self.felder[self.spalten_stand[stelle]][stelle] = spieler.farbe
                self.spielverlauf.append([self.spalten_stand[stelle],[stelle]])
                gewonnen = self.__check(spieler, self.spalten_stand[stelle], stelle)

                self.spalten_stand[stelle] += 1
                self.spielfeld_anzeigen()
                if(gewonnen):
                    return True
                break
            else:
                print("Spalte voll du Hong, such ne andere aus")
                self.spielfeld_anzeigen()

    def spielstein_einwerfen_test(self, spieler, stelle) -> bool:
        while(True):
            cls()
            if (self.spalten_stand[stelle] < self.hoehe):
                self.felder[self.spalten_stand[stelle]][stelle] = spieler.farbe
                self.spielverlauf.append([self.spalten_stand[stelle],[stelle]])
                gewonnen = self.__check(spieler, self.spalten_stand[stelle], stelle)

                self.spalten_stand[stelle] += 1
                self.spielfeld_anzeigen()
                if(gewonnen):
                    return True
                break
            else:
                print("Spalte voll du Hong, such ne andere aus")
                self.spielfeld_anzeigen()

    def __check(self, spieler, reihe, spalte):
        gewonnen = []
        gewonnen.append(self.__check_horizontal(spieler, reihe))
        gewonnen.append(self.__check_vertical(spieler, spalte))
        gewonnen.append(self.__check_diagonal_mirrored(spieler, reihe, spalte))
        gewonnen.append(self.__check_diagonal_up(spieler, reihe, spalte))

        return any(gewonnen)
    
    def __check_horizontal(self, spieler, reihe):
        vier_in_reihe = 0

        for i in range(self.breite):
            if vier_in_reihe == 4:
                return True
            if self.felder[reihe][i] == spieler.farbe:
                vier_in_reihe += 1
            else:
                vier_in_reihe = 0

        return False
    
    def __check_vertical(self, spieler, spalte):
        vier_in_reihe = 0

        for i in range(self.hoehe):
            if vier_in_reihe == 4:
                return True
            if self.felder[i][spalte] == spieler.farbe:
                vier_in_reihe += 1
            else:
                vier_in_reihe = 0

        return False

    def __check_diagonal_mirrored(self, spieler, reihe, spalte):
        upper_list_mirrored = feld.return_upper_coordinates_mirrored(reihe, spalte)
        lower_list_mirrored = feld.return_lower_coordinates_mirrored(reihe, spalte)
        coordinates_mirrored = upper_list_mirrored + lower_list_mirrored

        vier_in_reihe = 0
        for field in coordinates_mirrored:
            if self.felder[field[0]][field[1]] == spieler.farbe:
                vier_in_reihe += 1
            else:
                vier_in_reihe = 0
            if vier_in_reihe >= 4:
                return True

    def return_lower_coordinates_mirrored(self, reihe, spalte):
        lower = []

        while(reihe >= 1 and spalte != self.breite-1):
            reihe -= 1
            spalte += 1
            lower.append([reihe, spalte])

        return lower

    def return_upper_coordinates_mirrored(self, reihe, spalte):
        upper = []
        upper.append([reihe, spalte])

        while(reihe <= 4 and spalte != 0):
            reihe += 1
            spalte -= 1
            upper.append([reihe, spalte])
        return list(reversed(upper))

    def __check_diagonal_up(self, spieler, reihe, spalte):
        upper_list = feld.return_upper_coordinates(reihe, spalte)
        lower_list = feld.return_lower_coordinates(reihe, spalte)
        coordinates = upper_list + lower_list

        vier_in_reihe = 0
        for field in coordinates:
            if vier_in_reihe == 4:
                return True
            if self.felder[field[0]][field[1]] == spieler.farbe:
                vier_in_reihe += 1
            else:
                vier_in_reihe = 0
        
    def return_upper_coordinates(self, reihe, spalte):
        upper = []
        upper.append([reihe, spalte])

        while(reihe != 0 and spalte != 0):
            reihe -= 1
            spalte -= 1
            upper.append([reihe, spalte])
        return list(reversed(upper))

    def return_lower_coordinates(self, reihe, spalte):
        lower = []

        while(reihe != self.hoehe-1 and spalte != self.breite-1):
            reihe += 1
            spalte += 1
            lower.append([reihe, spalte])

        return lower

    
if __name__ == "__main__":
    debug = False
    spieler1 = Spieler("Levent", "R")
    spieler2 = Spieler("Spiro", "Y")

    spielzuege = [[6, 5], [5, 4], [3, 4], [4, 3], [2, 3], [3,1]]
    spielzuege2 = [[0,1], [1,2], [3, 2], [2,3], [4,3], [3,1]]
    feld = Spielfeld()

    if(debug):
        for zug in spielzuege2:
            win = feld.spielstein_einwerfen_test(spieler1, zug[0])
            if win:
                print(spieler1.name, "hat gewonnen")
                break
            win = feld.spielstein_einwerfen_test(spieler2, zug[1])
            if win:
                print(spieler2.name, "hat gewonnen")
                break
    else:
        for _ in range(21):
            win = feld.spielstein_einwerfen(spieler1)
            if win:
                print(spieler1.name, "hat gewonnen")
                break
            win = feld.spielstein_einwerfen(spieler2)
            if win:
                print(spieler1.name, "hat gewonnen")
                break

  

     