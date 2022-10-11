from dataclasses import dataclass


@dataclass
class TrainModelInput:
    commandSetPoint: float = 0.0
    authority: bool = False
    currentSetPoint: float = 0.0
    brakeFailure: bool = False
    signalPickupFailure: bool = False
    engineFailure: bool = False
    stationName: str = "YARD"