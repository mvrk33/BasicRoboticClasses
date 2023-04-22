import machine
import time

# set up ADC on channel 0
adc = machine.ADC(0)

# voltage divider resistances (in ohms)
R1 = 10000
R2 = 10000

# ADC reference voltage (in volts)
V_REF = 3.3

# convert ADC value to voltage
def adc_to_voltage(adc_val):
    return adc_val * V_REF / 65535 * (R1 + R2) / R2

while True:
    # read ADC value and convert to voltage
    adc_val = adc.read()
    voltage = adc_to_voltage(adc_val)
    
    # print voltage to console
    print("Voltage: {:.2f} V".format(voltage))
    
    # wait for a moment before reading again
    time.sleep(0.1)
