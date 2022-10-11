from dataclasses import dataclass


@dataclass
class PassengerInput:
    emergencyBrake: bool = False