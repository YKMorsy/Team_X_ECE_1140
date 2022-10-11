from dataclasses import dataclass


@dataclass
class TrainDriverOutput:
    currentSetPoint: float = 0.0
    speedLimit: float = 0.0
    interiorTemperature: int = 70
    commandSetPoint: float = 0.0
    brakeFailure: bool = False
    engineFailure: bool = False
    wheelFailure: bool = False
    signalPickUpFailure: bool = False
    authority: bool = False
    nextStop: str = ""