import machine
import time

servo_pin = machine.Pin(18)
pwm = machine.PWM(servo_pin)
pwm.freq(50)

while True:
    for duty_cycle in range(40, 131, 10):
        pwm.duty_u16(duty_cycle * 65535 // 100)
        print("a")
        time.sleep(0.50)
        print("s")
        time.sleep(0.100)
        print("s")
        time.sleep(0.500)
        print("s")
        time.sleep(1)
        print("s")
