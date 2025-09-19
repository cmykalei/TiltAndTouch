import smbus2

class Shield:

    def __init__(self, address=0x48, channels=4, vref=3.3, bus=1):
        self.address = address
        self.channels = channels
        self.vref = vref
        self.bus = smbus2.SMBus(bus)

    def read_raw(self, channel: int):
        if channel not in range(self.channels):
            raise ValueError("Channel must be 0-3")
        else:
            self.bus.write_byte(self.address, channel)
            self.bus.read_byte(self.address) # Note: Dummy-read!
            return self.bus.read_byte(self.address)

    def read_voltage_channel(self, channel: int):
        raw = self.read_raw(channel)
        return (raw / 255.0) * self.vref

    def read_voltage(self):
        return {ch: self.read_voltage_channel(ch) for ch in range(self.channels)}

    def read_pressure(self, channel: int, vmin: float, vmax: float, pmax: float):
        voltage = self.read_voltage_channel(channel)
        if voltage < vmin:
            return 0.0
        elif voltage > vmax:
            return pmax
        else:
            return ((voltage - vmin) / (vmax - vmin)) * pmax
