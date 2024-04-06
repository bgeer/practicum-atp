import unittest
import sys
sys.path.append('C:\projects\practicum-atp\simulator-Bas')
from Sensors import *
import actuators

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.tempSensor = TemperatureSensor(OneWireSlave(22.0))
        self.phSensor = OT3470(0x63, 0x01, I2CBus({0x63: {0x01: [ord(c) for c in str(12)]}}))
        self.heater = actuators.Heater()
        self.pump = actuators.Pump()
        
    def test_temperature_and_heater(self):
        temperature = self.tempSensor.read()
        if temperature > 20:
            self.heater.off()
            self.assertEqual(self.heater.get_state(), False, "Heater should be off")
        else:
            self.heater.on()
            self.assertEqual(self.heater.get_state(), True, "Heater should be on")

    def test_ph_and_pump(self):
        ph = self.phSensor.read()
        if ph > 10:
            self.pump.off()
            self.assertEqual(self.pump.get_state(), False, "Pump should be off")
        else:
            self.pump.on()
            self.assertEqual(self.pump.get_state(), True, "Pump should be on")

if __name__ == '__main__':
    unittest.main()