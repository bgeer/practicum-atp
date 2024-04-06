from decorators import *
from Constants import *


class Controller:
    def __init__(self= None, Pump = None, Heater = None, tempSensor = None, phSensor = None, thresholdTemp = 20, thresholdPh = 10) -> None:
        self.heater = Heater
        self.pump = Pump
        self.tempSensor = tempSensor
        self.phSensor = phSensor
        self.tempThreshold = thresholdTemp
        self.phThreshold = thresholdPh
    
    @log_execution_to_file(LOG_FILE)
    def update(self):
        if self.heater.get_state() & (self.tempSensor.read() > self.tempThreshold):
            self.heater.off()
        elif not self.heater.get_state() & (self.tempSensor.read() < self.tempThreshold):
            self.heater.on()
        if self.pump.get_state() & (self.phSensor.read() > self.phThreshold):
            self.pump.off()
        elif not self.pump.get_state() & (self.phSensor.read() < self.phThreshold):
            self.pump.on()