## What is It?

LED: Light Emitting Diode

LED is something that creates light as electric flows throught it.

### Features of LED

- Diode: A semiconductor device that allows current to flow in only one direction.
- Light emission: When current passes through the diode, it releases energy in the form of photons (light).

## The Standard of Connecting a LED with a Breadboard and a Pico

### Materials Needed

- Raspberry Pi Pico
- Breadboard
- LED
- Resistor (220Ω to 330Ω is typical)
- Jumper wires

### How to Connect

Place the LED on the Breadboard:

- The long leg is the anode (+). Connect this to the GPIO pin on the Pico.
- The short leg is the cathode (–). This goes to GND through a resistor.

Place a 220Ω resistor in series with the LED to prevent it from burning out.
