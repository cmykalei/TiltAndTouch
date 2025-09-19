# Pi-venv
When `activate`, the update function will send the folder over (rsync), then run the program specified by the <module> parameter. The script function 'update <module>' assumes the Raspberry Pi username is the same as the local's `$USER`.

**These are not instructions.**

## Tools used
- Raspberry Pi 5
- Raspberry Pi OS Lite
- Duinotech Raspberry Pi GPIO Expansion Shield with 4 x AD/DA
- Arduino Compatible Thin-Film Pressure Sensor
- Breadboard
- Some jumper cables (female-to-male)

## Setup
```
ssh pi
mkdir gpio
cd gpio
sudo apt update
sudo apt install python3-venv
python3 -m venv gpio-venv
sudo apt install gpiod libgpiod-dev
sudo apt install i2c-tools python3-smbus
sudo usermod -aG gpio $USER
sudo raspi-config
i2cdetect -y 1
```

## Script
```
mkdir scripts
nano scripts/activate.sh

#!/bin/sh
PROJECT="gpio"
source "${PROJECT}-venv/bin/activate"

alias doit="python3 ${PROJECT}.py"
```
_Then CTRL+X and Y._

## Activate
```
source scripts/activate.sh
pip install adafruit-circuitpython-ads1x15
pip install smbus2
```

## Results
```
thin_film_pressure_sensor: 0.25 kg (Voltage: 1.15 V)
thin_film_pressure_sensor: 0.00 kg (Voltage: 0.27 V)
thin_film_pressure_sensor: 0.00 kg (Voltage: 0.03 V)
thin_film_pressure_sensor: 0.00 kg (Voltage: 0.01 V)
thin_film_pressure_sensor: 0.00 kg (Voltage: 0.01 V)
thin_film_pressure_sensor: 0.00 kg (Voltage: 0.04 V)
thin_film_pressure_sensor: 0.00 kg (Voltage: 0.00 V)
thin_film_pressure_sensor: 0.39 kg (Voltage: 2.14 V)
thin_film_pressure_sensor: 0.34 kg (Voltage: 1.94 V)
thin_film_pressure_sensor: 0.02 kg (Voltage: 0.22 V)
thin_film_pressure_sensor: 0.03 kg (Voltage: 0.17 V)
```





