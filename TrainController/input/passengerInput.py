from dataclasses import dataclass


@dataclass
class PassengerInput:
    emergency_brake: bool = False