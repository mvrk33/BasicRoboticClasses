import machine
import time

# ADC pin connected to the temperature sensor
temperature_pin = machine.ADC(26)  # Example ADC pin number, modify according to your setup

# ADC voltage reference set to 3.3V
adc_reference_voltage = 3.3

# Temperature calibration values (specific to your temperature sensor)
calibration_factor = 10.0  # Example calibration factor, modify according to your sensor

# Function to convert ADC value to temperature
def adc_to_temperature(adc_value):
    voltage = adc_value * (adc_reference_voltage / 65535)  # Convert ADC value to voltage
    temperature = voltage * calibration_factor  # Convert voltage to temperature using calibration factor
    return temperature

# Main loop
while True:
    adc_value = temperature_pin.read_u16()  # Read ADC value
    temperature = adc_to_temperature(adc_value)  # Convert ADC value to temperature
    print("Temperature: {:.2f}°C".format(temperature))

    time.sleep(1)  # Delay for 1 second

