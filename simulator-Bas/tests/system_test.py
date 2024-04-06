import unittest
import sys
sys.path.append('C:\projects\practicum-atp\simulator-Bas')
from Sensors import *
import actuators
from Controller import *


class testSystem(unittest.TestCase):
    def setUp(self):
        self.tempSensor = TemperatureSensor(OneWireSlave(18.0))
        self.phSensor = OT3470(0x63, 0x01, I2CBus({0x63: {0x01: [ord(c) for c in str(12)]}}))
        self.heater = actuators.Heater()
        self.pump = actuators.Pump()
        self.controller = Controller(Heater=self.heater, 
                                     Pump=self.pump, 
                                     tempSensor=self.tempSensor, 
                                     phSensor=self.phSensor,
                                     thresholdTemp=20,
                                     thresholdPh=10)

    def test_system(self):
        self.controller.update()
        self.assertEqual(self.heater.get_state(), True, "Heater should be on")
        self.assertEqual(self.pump.get_state(), True, "Pump should be on")


if __name__ == '__main__':
    unittest.main()