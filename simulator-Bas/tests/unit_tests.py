import unittest
import sys
sys.path.append('C:\projects\practicum-atp\simulator-Bas')

from Sensors import *

class testOneWireSlave(unittest.TestCase):
    def test_set_temperature(self):
        slave = OneWireSlave(11.0)
        self.assertIsNone(slave.set_temperature(12.0))
        self.assertEqual(slave.get_temperature(), 12.0, "Temperature should be 12.0")

    def test_get_temperature(self):
        slave = OneWireSlave(11.0)
        self.assertIsInstance(slave.get_temperature(), float, "Temperature should be a float")
        self.assertEqual(slave.get_temperature(), 11.0, "Temperature should be 11.0")

class testTemperatureSensor(unittest.TestCase):
    def test_read(self):
        slave = OneWireSlave(11)
        sensor = TemperatureSensor(slave)
        self.assertIsInstance(sensor.read(), float, "Temperature should be a float")
        self.assertEqual(sensor.read(), 11, "Temperature should be 11")

class testOT3470(unittest.TestCase):
    def test_read(self):
        i2c = I2CBus({0x63: {0x01: [ord(c) for c in str(7)]}})
        sensor = OT3470(0x63, 0x01, i2c)
        self.assertIsInstance(sensor.read(), float, "pH should be a float")
        self.assertEqual(sensor.read(), 7, "pH should be 7")

if __name__ == '__main__':
    unittest.main()