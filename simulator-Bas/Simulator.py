from Sensors import *
from Controller import *
from time import sleep
import actuators
from decorators import *
from Constants import *


class Plant():
    def __init__(self) -> None:
        self.temp = initialTemperature
        self.ph = initialPh
        self.I2CBus = I2CBus({0x63: {0x01: [ord(c) for c in str(self.ph)]}})
        self.phSensor = OT3470(0x63, 0x01, self.I2CBus)
        self.heater = actuators.Heater()
        self.pump = actuators.Pump()
        self.OneWireSlave = OneWireSlave(self.temp)
        self.tempSensor = TemperatureSensor(self.OneWireSlave)

    @log_execution_to_file(LOG_FILE)
    def update(self):
        if self.heater.get_state():
            self.temp += temperatureIncrease
        else:
            self.temp -= random.uniform(0.05, temperatureDecay)
        self.temp = round(self.temp, 2)
        self.update_temp()

        if self.pump.get_state():
            self.ph += phIncrease
        else:
            self.ph -= random.uniform(0.05, phDecay)
        self.ph = round(self.ph, 2)
        self.update_ph()

    @log_execution_to_file(LOG_FILE)
    def update_temp(self):
        #write simulated temperature to DSB1820 memory
        self.OneWireSlave.set_temperature(self.temp)

    @log_execution_to_file(LOG_FILE)
    def update_ph(self):
        #write simulated pH to OT3470 bus and correct register
        raw_ph = [ord(c) for c in str(self.ph)]
        self.I2CBus.write(0x63, 0x01, raw_ph)


    def print_state(self):
        print(f'Temperature: {self.temp}')
        print(f'pH: {self.ph}')
        print('Heater: '+ ('On' if self.heater.get_state() else 'Off'))
        print('Pump: '+ ('On' if self.pump.get_state() else 'Off'))

class Simulator():
    def __init__(self) -> None:
        self.plant = Plant()
        self.controller = Controller(Heater=self.plant.heater, 
                                     Pump=self.plant.pump, 
                                     tempSensor=self.plant.tempSensor, 
                                     phSensor=self.plant.phSensor)

    def run(self):
        timestamp = 0
        while True:
            timestamp += 1
            self.plant.update()
            self.controller.update()
            print('-' * 8, 'Plant State', '-' * 8, "Timestamp:", timestamp, '-' * 4)
            self.plant.print_state()
            sleep(sleepTime)