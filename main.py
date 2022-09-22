from draw import Grill
import time

class Boss:
    def __init__(self):
        self.grill = Grill()
        time.sleep(3)

if __name__ == '__main__':
    Boss()