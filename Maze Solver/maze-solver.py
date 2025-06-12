import network
import socket
from machine import Pin, PWM, time_pulse_us
import time

SSID = 'direnev'
PASSWORD = '3562149160'

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    time.sleep(1)

ip = wlan.ifconfig()[0]
print("Connected to WiFi. IP:", ip)

# Motor and LED Setup
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
TRIG = Pin(8, Pin.OUT)
ECHO = Pin(9, Pin.IN)

def stop():
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)

def forward():
    IN1.value(0)
    IN2.value(1)
    IN3.value(1)
    IN4.value(0)

def backward():
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)

def left():
    IN1.value(1)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)

def right():
    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(1)

def getDistance():
    TRIG.low()
    time.sleep(0.002)
    TRIG.high()
    time.sleep(0.00001)
    TRIG.low()
    duration = time_pulse_us(ECHO, 1, 30000)

    if duration <= 0:
        return -1
    
    distance = (duration * 0.0343) / 2
    return distance

# HTML page
html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>HISAR PICO-CAR</title>
  <style>
    *{margin:0;padding:0;box-sizing:border-box;}
    .full-screen{height:100vh;width:100vw;background:#a4ffac;display:flex;justify-content:center;align-items:center;font-family:'Comic Sans MS',cursive;}
    .text{color:darkgreen;font-size:24px;}
    .image{height:100px;width:100px;cursor:pointer;}
    .led{position:absolute;left:50%;transform:translateX(-50%);top:10px;color:#a4ffac;background:rgb(20,155,20);font-family:'Comic Sans MS',cursive;}
    .led:hover{cursor:pointer;}
    .up{position:absolute;left:50%;bottom:10px;transform:translate(-50%,-110%);}
    .up:hover{transform:translate(-50%,-110%) scale(1.05);}
  </style>
  <script>
    const PICO_IP = window.location.origin;
    function sendCommand(direction) {
      fetch(`${PICO_IP}/${direction}`)
        .then(response => response.text())
        .then(data => console.log(data))
        .catch(err => console.error('Error:', err));
    }
  </script>
</head>
<body>
  <div class="full-screen">
    <div class="text">HISAR PICO-CAR MAZE-FINDER</div>
    <img class="image up" onclick="sendCommand('start')" src="https://github.com/keremdiren1/Hisar-Pico-Car/blob/main/web/images/upArrow.png?raw=true">
    <div class="led" onclick="sendCommand('stop')">STOP</div>
  </div>
</body>
</html>
"""

# Server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print("Listening on", addr)
print("Waiting for connections...")

doStart = False
wentRight = False
stop()
while True:
    cl, addr = s.accept()
    request = cl.recv(1024).decode()
    print("Client connected from", addr)
    print("Request:", request)

    if 'GET /start' in request:
        doStart = True
        wentRight = False
        cl.send('HTTP/1.0 200 OK\r\nContent-Type: text/plain\r\n\r\nOK')
    else:
        cl.send('HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n' + html)
    
    while doStart:
        forward()
        distance = getDistance()
        
        if distance > -1 and distance < 15:
            if not wentRight:
                right()
                time.sleep(1)
            else:
                left()
                time.sleep(1)
            
            wentRight = True
        else:
            wentRight = False
        
        if 'GET /stop' in request:
            doStart = False
            stop()
            cl.send('HTTP/1.0 200 OK\r\nContent-Type: text/plain\r\n\r\nOK')

    cl.close()

