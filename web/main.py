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

in1 = Pin(2, Pin.OUT)
in2 = Pin(3, Pin.OUT)
ena_pwm = PWM(Pin(4))
ena_pwm.freq(1000)
ena_pwm.duty_u16(40000)
led = Pin(15, Pin.OUT)

def stop():
    in1.low()
    in2.low()

def forward():
    in1.high()
    in2.low()

def backward():
    in1.low()
    in2.high()

def left():
    in1.low()
    in2.high()

def right():
    in1.high()
    in2.low()

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