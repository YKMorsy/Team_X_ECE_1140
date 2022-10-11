from dataclasses import dataclass


@dataclass
class EngineerInput:
    Kp: float = 1.0
    Ki: float = 1.0