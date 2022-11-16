from dataclasses import dataclass


@dataclass
class EngineerInput:
    kp: float = 1.0
    ki: float = 1.0