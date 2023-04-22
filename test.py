import machine

button_pin = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button_pin.value() == 1:
        print("Button pressed")





