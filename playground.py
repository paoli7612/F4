class Playground(list):
    def __init__(self):
        for n in range(5):
            self.append([0]*7)

    def __str__(self):
        r = ""
        for n in self:
            r += str(n) + "\n"
        return r