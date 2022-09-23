from draw import Grill

class Match:
    def __init__(self):
        self.grill = Grill()
        self.turn = True

    def start(self):
        self.running = True
        while self.running:
            x = self.grill.get_choice()
            y = 5
            self.grill.token(self.turn, x, y)