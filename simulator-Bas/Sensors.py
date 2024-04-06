import random
from decorators import *
from Constants import *

class TemperatureSensor:  # Temperature sensor
    def __init__(self, one_wire_slave=None):
        self.one_wire_slave = one_wire_slave
        pass

    @log_execution_to_file(LOG_FILE)
    def read(self):
        raw = self.one_wire_slave.perform_function('READ_SCRATCHPAD')
        return self.decode(raw)        
    
    # Function to convert a 12-bit raw reading to Celsius
    @log_execution_to_file(LOG_FILE)
    def decode(self, raw):
        # Extract the bits
        sign_bit = (raw >> 11) & 0x01
        absolute_temperature = raw & 0x07FF

        # Calculate temperature in Celsius
        resolution = 0.0625
        self.temperature = -absolute_temperature * resolution if sign_bit == 1 else absolute_temperature * resolution

        return self.temperature


class OneWireSlave:
    def __init__(self, temperature=0.0):
        self.temperature = temperature
        pass

    @log_execution_to_file(LOG_FILE)
    def perform_function(self, function_command):
        if function_command == 'READ_SCRATCHPAD':
            return self.generate_12_bit_reading(self.temperature)
        else:
            return "Function not supported"
        #other commands not implemented yet

    @log_execution_to_file(LOG_FILE)
    def set_temperature(self, temperature):
        self.temperature = temperature

    @log_execution_to_file(LOG_FILE)
    def get_temperature(self):
        return self.temperature
    
     # Function to generate a 12-bit raw reading
    @log_execution_to_file(LOG_FILE)
    def generate_12_bit_reading(self, temperature):
        # Convert the temperature to a 12-bit raw reading
        resolution = 0.0625
        sign_bit = 1 if temperature < 0 else 0
        absolute_temperature = abs(temperature)

        raw_reading = int(absolute_temperature / resolution)
        twelve_bit_value = (sign_bit << 11) | raw_reading

        return twelve_bit_value
    
class I2CBus:
    def __init__(self, data):
        self.data = data

    @log_execution_to_file(LOG_FILE)
    def write(self, address, register, value):
        self.data[address][register] = value

    @log_execution_to_file(LOG_FILE)
    def read(self, address, register):
        return self.data[address][register]

class OT3470:
    def __init__(self, address, register, bus= None):
        self.bus = bus
        self.address = address
        self.register = register
        pass

    @log_execution_to_file(LOG_FILE)
    def read(self):
        return self.decode(self.bus.read(self.address, self.register))
    
    @log_execution_to_file(LOG_FILE)
    def decode(self, raw):
        # Convert the raw reading to a string
        value = ''.join([chr(c) for c in raw])
        return float(value) 