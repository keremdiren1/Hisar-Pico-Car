from machine import Pin, PWM
import time

IN1 = Pin(2, Pin.OUT)
IN2 = Pin(3, Pin.OUT)
ENA = PWM(Pin(4))

ENA.freq(1000)

def motor_forward(speed):
    IN1.value(1)
    IN2.value(0)
    ENA.duty_u16(speed)

def motor_backward(speed):
    IN1.value(0)
    IN2.value(1)
    ENA.duty_u16(speed)

def motor_stop():
    ENA.duty_u16(0)

while True:
    motor_forward(45000)
    time.sleep(0.5)
    motor_stop()
    time.sleep(1)
    motor_backward(45000)
    time.sleep(0.5)
    motor_stop()
    time.sleep(2)
