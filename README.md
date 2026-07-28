# Raspberry Pi Pico 2 W Alarm Clock
A digital alarm clock built with a Raspberry Pi Pico 2 W and MicroPython. 
It displays the current time on a 16x2 I2C LCD and activates a passive buzzer when the selected alarm time is reached.

## Features

- The current hour, minute and second can be set through the console, along with the alarm time.
- When the clock reaches the selected alarm time, the passive buzzer plays a 2000 Hz tone for ten seconds.

## Hardware

- Raspberry Pi Pico 2 W
- 16x2 LCD with I2C interface
- Passive buzzer
- Female-to-female jumper wires

## Pin connections

| Component | Pico connection |
|---|---|
| LCD SDA | GP4 (physical pin 6) |
| LCD SCL | GP5 (physical pin 7) |
| LCD GND | GND (physical pin 8) |
| LCD VCC | VSYS (physical pin 39) |
| Passive buzzer signal | GP15 (physical pin 20) |
| Passive buzzer ground | GND |

## Software

- MicroPython
- Thonny IDE
- `I2C_LCD` library for controlling the LCD

## How it works

The clock advances once per second using `ticks_ms()` and `ticks_diff()`. 
The current time is shown on the LCD, and the buzzer produces a 2000 Hz tone for ten seconds when the selected alarm time is reached.

A future version is planned to use physical controls, allowing the clock and alarm to be configured directly on the device without a connected computer.

## Dependencies and credits

This project uses Freenove's `I2C_LCD` MicroPython library to control the LCD. The library is not included in this repository.

The LCD library is licensed under CC BY-NC-SA 3.0. The alarm clock logic in `main.py` is my own work.

## Project status

Working prototype. The clock, LCD display and alarm buzzer are functioning, but the current time and alarm time must still be entered through a connected computer.

## Planned improvements

- Physical buttons for setting the time and alarm
- Alarm on/off control
- Menu system shown on the LCD
- Alternating buzzer tones using two different frequencies
- Portable power supply
- 3D-printed enclosure

## Running the project

1. Connect the Raspberry Pi Pico 2 W to a computer using USB.
2. Open `main.py` in Thonny.
3. Make sure the `I2C_LCD` library is installed on the Pico.
4. Run the program.
5. Enter the current hour, minute and second in the console.
6. Enter the desired alarm hour and minute.
