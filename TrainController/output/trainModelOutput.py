from dataclasses import dataclass


@dataclass
class TrainModelOutput:
    service_brake: bool = False
    engine_power: float = 0.0
    emergency_brake: bool = False
    left_side_doors: bool = False
    right_side_doors: bool = False
    announce_stop: bool = False
    inside_lights: bool = False
    outside_lights: bool = False
    activate_announcement: bool = False