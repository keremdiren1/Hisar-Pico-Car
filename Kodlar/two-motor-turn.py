from machine import Pin, PWM
import time

IN1 = Pin(2, Pin.OUT)
IN2 = Pin(3, Pin.OUT)
ENA = PWM(Pin(4))
IN3 = Pin(5, Pin.OUT)
IN4 = Pin(6, Pin.OUT)
ENB = PWM(Pin(7))

ENA.freq(1000)
ENB.freq(1000)

def motor_forward(speed):
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)
    ENA.duty_u16(speed)
    ENB.duty_u16(speed)

def motor_backward(speed):
    IN1.value(0)
    IN2.value(1)
    IN3.value(1)
    IN4.value(0)
    ENA.duty_u16(speed)
    ENB.duty_u16(speed)

def motor_stop():
    ENA.duty_u16(0)
    ENB.duty_u16(0)

while True:
    motor_forward(50000)
    time.sleep(2)
    motor_stop()
    time.sleep(1)
    
    motor_backward(50000)
    time.sleep(2)
    motor_stop()
    time.sleep(2)