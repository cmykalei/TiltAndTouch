class PressureSensor:
    def __init__(self, name: str, channel: int, vmin: float, vmax: float, pmax: float, unit: str="kg"):
        self.name = name
        self.channel = channel
        self.vmin = vmin
        self.vmax = vmax
        self.pmax = pmax
        self.unit = unit

    def calibration(self):
        return self.vmin, self.vmax, self.pmax
