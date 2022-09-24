import time
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
            return True

    def start(self):
        self.running = True
        while self.running:
            # Se qualcuno ha vinto
            if self.win():
                break

            # Prendi colonna in input
            try:
                x = self.grill.get_choice()
            except: # Se non riesce chiude la finestra
                self.running = False
                continue

            # Inserisci gettone nella colonna
            try:
                y = self.playground.token(self.turn, x)
                self.grill.token(self.turn, x, y)
                self.next_turn()
            except: # Se non riescce la colonna è piena
                print("Colonna piena")
        time.sleep(2)
    
    def next_turn(self):
        self.turn = 3 - self.turn
