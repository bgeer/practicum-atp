from Simulator import *
from Constants import *

if __name__ == "__main__":
    # Clear the log file
    open(LOG_FILE, 'w').close()
    from Simulator import Simulator
    simulator = Simulator()
    simulator.run()