from settings import Refr


def isWin(a, b, c, d):
    if (a == b == c == d):
        return a
    else: 
        return Refr.EMPTY

class Playground(list):
    def __init__(self):
        for _ in range(6):
            self.append([Refr.EMPTY]*7)

    def __str__(self):
        r = ""
        for n in self:
            r += str(n) + "\n"
        return r

    def token(self, turn, x):
        print(self)
        for y in range(6):
            y = 5-y
            print("Provo y = " + str(y) + " e x = " + str(x))
            if self[y][x] == Refr.EMPTY:
                self[y][x] = turn
                return y
        raise Exception("Colonna piena")


    def win(self):
        for y in range(6):
            for x in range(4):
                if isWin(self[y][x+0], self[y][x+1], self[y][x+2], self[y][x+3]):
                    print("Riga" + str(y) + " a partire dalla colonna " + str(x))
