import machine
import time

adc = machine.ADC(0)  # create an ADC object on ADC channel 0
pin = machine.Pin(26, machine.Pin.IN)  # set up Pin 26 as an input

while True:
    reading = adc.read_u16()  # read the ADC value as an unsigned 16-bit integer
    voltage = reading * 3.3 / 65535  # convert the ADC value to a voltage
    print("ADC value: {:d}, voltage: {:.2f}V".format(reading, voltage))
    time.sleep(1)  # wait for 1 second before taking the next reading
