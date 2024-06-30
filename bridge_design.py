# Implementor
class Protocol:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


# Concrete Implementors
class WiFiProtocol(Protocol):
    def turn_on(self):
        print("Turning on device via WiFi")

    def turn_off(self):
        print("Turning off device via WiFi")


class ZigbeeProtocol(Protocol):
    def turn_on(self):
        print("Turning on device via Zigbee")

    def turn_off(self):
        print("Turning off device via Zigbee")


# Abstraction
class Device:
    def __init__(self, protocol):
        self.protocol = protocol

    def turn_on(self):
        self.protocol.turn_on()

    def turn_off(self):
        self.protocol.turn_off()


# Refined Abstractions
class Light(Device):
    def __init__(self, protocol):
        super().__init__(protocol)

    def dim(self, level):
        print(f"Dimming light to {level}% via {self.protocol.__class__.__name__}")


class Thermostat(Device):
    def __init__(self, protocol):
        super().__init__(protocol)

    def set_temperature(self, temperature):
        print(
            f"Setting temperature to {temperature}°C via {self.protocol.__class__.__name__}"
        )


# Usage
wifi_protocol = WiFiProtocol()
zigbee_protocol = ZigbeeProtocol()

# Control a light using different protocols
light = Light(wifi_protocol)
light.turn_on()
light.dim(50)
light.turn_off()

print("---")

light = Light(zigbee_protocol)
light.turn_on()
light.dim(70)
light.turn_off()

print("---")

# Control a thermostat using different protocols
thermostat = Thermostat(wifi_protocol)
thermostat.turn_on()
thermostat.set_temperature(22)
thermostat.turn_off()

print("---")

thermostat = Thermostat(zigbee_protocol)
thermostat.turn_on()
thermostat.set_temperature(18)
thermostat.turn_off()
