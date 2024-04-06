# Test Report

## Unit Tests
The unit tests can be found [here](unit_tests.py).
### testOneWireSlave
This unit test is to test the OneWireSlave device. The goal of this test is to check if it is possible to set a simulated temperature and read this temperature.

*After running the tests we can conclude the tested function used in the unit test are working correctly. All tests are passed.*

### testTemperatureSensor
This unit test is to test the Temperature Sensor. The goal of this test is to check if the recievew raw value can be decoded to a workable value.

*After running the test we can conclude that the function is working. The raw value is converted to a workable value which we can use in further steps of the system. The function returns a float.*

### testOT3470
This unit test is to test the ph Sensor. The goal of this test is to check if the recievew raw value can be decoded to a workable value.

*After running the test we can conclude that the function is working. The raw PH reading is decoded to a workable value. This value can be used later in the control unit to regulate the ph value in the fishtank*

## Integration Tests
The integration tests can be found [here](integration_tests.py).
### TestIntegration
This integration test is to test if the heater is turned on when the temperature is below a certain point. Same for the ph value, if that is under a certain point the pump will be turned on

*After running the integration test. The heater gets turned off and on at the right moments. Also the pump is tested based on the pH value. The pump also gets turned on and off at the right moment.* 

## System Tests
The system tests can be found [here](system_test.py).
### testSystem
This system test is to test the complete system including the controller. With all the components connected the system can control the temperature and ph in an aquarium.

*In the system test are all components put together in the control unit. The test result is positive because the heater and pump are turned on by the control unit. The initialized temperature and ph value are below the threshold so they should be turned on and that is what happens.* 


## Conclusion
Based on all these tests that are passed we can conclude that the system is working as expected ann the criteria and quality's are met. After adjustments to the code these test should be run again to check if the system is still working correctly. 