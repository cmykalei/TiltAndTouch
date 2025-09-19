try:
    print("Starting gpio.py...")
    import time

    print("Importing GPIO Shield...")
    from gpio_shield import Shield
    shield = Shield()

    print("Importing Pressure Sensor...")
    from gpio_sensor import PressureSensor
    pressure_sensor = PressureSensor(
        name="thin_film_pressure_sensor",
        channel=0,
        vmin=0.03,
        vmax=2.8,
        pmax=0.5,
        unit="kg"
    )

    print("Running GPIO test...")
    while True:
        voltage = shield.read_voltage_channel(pressure_sensor.channel)
        force = shield.read_pressure(pressure_sensor.channel, *pressure_sensor.calibration())
        print(f"{pressure_sensor.name}: {force:.2f} {pressure_sensor.unit} (Voltage: {voltage:.2f} V)")
        time.sleep(0.5)

    print("Done!\n")

except RuntimeError:
    print("Error importing RPi.GPIO!\n")
    print("You may have to run this script with 'sudo'.\n")
