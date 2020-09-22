from abc import ABC, abstractmethod
from random import randint
from time import sleep


class Sensor(ABC):
    """
    Implementations interface
    """
    @abstractmethod
    def measure(self):
        pass

    @abstractmethod
    def to_metric_system(self):
        pass


class TemperatureSensor(Sensor):
    """
    Concrete Implementation
    """
    def measure(self):
        print('measuring temperature')
        self.measurement = randint(32, 210)

    def to_metric_system(self):
        print('converting from °F to °C')
        return (self.measurement - 32) * 5 / 9


class VolumeSensor(Sensor):
    """
    Concrete Implementation
    """
    def measure(self):
        print('measuring volume')
        self.measurement = randint(0, 10)

    def to_metric_system(self):
        print('converting from gallon to litres')
        return self.measurement * 3.785


class Monitor:
    """
    Abstraction
    """
    def __init__(self, sensor):
        self.sensor = sensor

    def read_measurement(self):
        self.sensor.measure()

    def display_values(self):
        return self.sensor.to_metric_system()


class ControlSystem:
    """
    Client
    """
    def __init__(self):
        self.temperature_monitor = Monitor(TemperatureSensor())
        self.volume_monitor = Monitor(VolumeSensor())

    def run(self):
        print('Starting SCADA...')
        while True:
            self.activate_monitors()
            sleep(1)

    def activate_monitors(self):
        for monitor in self.temperature_monitor, self.volume_monitor:
            monitor.read_measurement()
            print(monitor.display_values())
            print('-----------------')


# USAGE
ControlSystem().run()
