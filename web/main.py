import network
import socket
from machine import Pin, PWM
import time

SSID = 'your_SSID'
PASSWORD = 'your_PASSWORD'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    time.sleep(1)

ip = wlan.ifconfig()[0]
print("Connected to WiFi. IP:", ip)

IN1 = Pin(2, Pin.OUT)
IN2 = Pin(3, Pin.OUT)
ENA = PWM(Pin(4))
IN3 = Pin(5, Pin.OUT)
IN4 = Pin(6, Pin.OUT)
ENB = PWM(Pin(7))
ENA.freq(1000)
ENA.duty_u16(50000)
ENB.freq(1000)
ENB.duty_u16(50000)
led = Pin(15, Pin.OUT)

def stop():
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)

def forward():
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)

def backward():
    IN1.value(0)
    IN2.value(1)
    IN3.value(1)
    IN4.value(0)

def left():
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)

def right():
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

while True:
    cl, addr = s.accept()
    request = cl.recv(1024).decode()
    print("Request:", request)

    if 'GET /up' in request:
        forward()
    elif 'GET /down' in request:
        backward()
    elif 'GET /left' in request:
        left()
    elif 'GET /right' in request:
        right()
    elif 'GET /led' in request:
        led.toggle()
    else:
        stop()

    cl.send('HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\nOK')
    cl.close()
