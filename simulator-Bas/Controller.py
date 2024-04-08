from decorators import *
from Constants import *


class Controller:
    def __init__(self= None, Pump = None, Heater = None, tempSensor = None, phSensor = None, thresholdTemp = 28, thresholdPh = 7) -> None:
        self.heater = Heater
        self.pump = Pump
        self.tempSensor = tempSensor
        self.phSensor = phSensor
        self.tempThreshold = thresholdTemp
        self.phThreshold = thresholdPh
    
    @log_execution_to_file(LOG_FILE)
    def update(self):
        currentTemp = self.tempSensor.read()
        currentPh = self.phSensor.read()
        stateHeater = self.heater.get_state()
        statePump = self.pump.get_state()
        if stateHeater & (currentTemp > self.tempThreshold):
            self.heater.off()
        elif not stateHeater & (currentTemp < self.tempThreshold):
            self.heater.on()
        if statePump & (currentPh > self.phThreshold):
            self.pump.off()
        elif not statePump & (currentPh < self.phThreshold):
            self.pump.on()