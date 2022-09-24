from draw import Grill
from playground import Playground

class Match:
    def __init__(self):
        self.grill = Grill()
        self.turn = True
        self.playground = Playground()

    def start(self):
        self.running = True
        while self.running:
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
        self.turn = not self.turn
