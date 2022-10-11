from dataclasses import dataclass


@dataclass
class TrainDriverInput:
    commandSetPoint: float = 0.0
    serviceBrake: bool = False
    emergencyBrake: bool = False
    manualMode: bool = False
    interiorTemperatureControl: int = 70
    insideLights: bool = False
    outsideLights: bool = False
    rightSideDoors: bool = False
    leftSideDoors: bool = False
    activateAnnouncement: bool = False
