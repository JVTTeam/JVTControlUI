import config
import device_interface


class StimulationController:
    ZONE_IDS = map(chr, range(ord("I"), ord("W") + 1))

    stimulation = dict()

    def __init__(self) -> None:
        self.device = device_interface.SerialInterface(config.COM_PORT, config.BAUDRATE)

    def update_stimulation(self, zone, strength, frequency, pulse_width):
        if (
            zone in self.stimulation
            and self.frequency == frequency
            and self.pulse_width == pulse_width
        ):
            self.stimulation.pop(zone, None)
        else:
            self.stimulation[zone] = strength
            self.frequency = frequency
            self.pulse_width = pulse_width

        self.transfer()

    def clear_stimulation(self):
        self.stimulation.clear()
        self.transfer()

    def serialize_stimulation(self):
        serial = ""
        for zone, strength in self.stimulation.items():
            serial += f"{zone}{strength}"

        serial += f"X{self.frequency}Y{self.pulse_width}\n"
        return serial

    def transfer(self):
        serial = self.serialize_stimulation()
        self.device.write(serial)

        print(f"Transferred: {serial.strip()}")
