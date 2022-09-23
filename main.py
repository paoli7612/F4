from match import Match
import time

class Boss:
    def __init__(self):
        Match().start()
        time.sleep(3)

if __name__ == '__main__':
    Boss()