from dataclasses import dataclass


@dataclass
class EngineerInput:
    kp: float = 200.0
    ki: float = 250.0