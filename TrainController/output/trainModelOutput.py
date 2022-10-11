from dataclasses import dataclass


@dataclass
class TrainModelOutput:
    serviceBrake: bool = False
    enginePower: float = 0.0
    emergencyBrake: bool = False
    leftSideDoors: bool = False
    rightSideDoors: bool = False
    announceStop: bool = False
    insideLights: bool = False
    outsideLights: bool = False
    activateAnnouncement: bool = False