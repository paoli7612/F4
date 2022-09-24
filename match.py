from draw import Grill
from playground import Playground

class Match:
    def __init__(self):
        self.grill = Grill()
        self.turn = 1
        self.playground = Playground()

    def win(self):
        w = self.playground.win()          
        if w:
            self.grill.win(w)
            self.running = False

    def start(self):
        self.running = True
        while self.running:
            if self.win():
                break
            try:
                x = self.grill.get_choice()
            except:
                self.running = False
                continue
            try:
                y = self.playground.token(self.turn, x)
                self.grill.token(self.turn, x, y)
                self.next_turn()
            except:
                print("Colonna piena")

    
    def next_turn(self):
        self.turn = 3 - self.turn
