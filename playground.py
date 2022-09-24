from settings import Opt, Refr


def isWin(a, b, c, d):
    if (a == b == c == d):
        return a
    else: 
        return Refr.EMPTY

class Playground(list):
    def __init__(self):
        for _ in range(Opt.Window.NY):
            self.append([Refr.EMPTY]*Opt.Window.NX)

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
        for y in range(Opt.Window.NY):
            for x in range(Opt.Window.NX):
                # Controllo vittoria orizzontale
                try:
                    if isWin(self[y][x+0], self[y][x+1], self[y][x+2], self[y][x+3]):
                        return (x, y, Refr.O)
                except: pass
                # Controllo vittoria verticale
                try:
                    if isWin(self[y+0][x], self[y+1][x], self[y+2][x], self[y+3][x]):
                        return (x, y, Refr.V)
                except: pass
