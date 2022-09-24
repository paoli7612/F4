class Playground(list):
    def __init__(self):
        for _ in range(6):
            self.append([-1]*7)

    def __str__(self):
        r = ""
        for n in self:
            r += str(n) + "\n"
        return r

    def token(self, turn, x):
        print(self)
        for y in range(5):
            y = 5-y
            print("Provo y = " + str(y) + " e x = " + str(x))
            if self[y][x] == -1:
                self[y][x] = turn
                return y
        raise Exception("Colonna piena")
