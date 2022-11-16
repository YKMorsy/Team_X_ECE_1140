from dataclasses import dataclass


@dataclass
class TrainDriverInput:
    command_set_point: float = 0.0
    service_brake: bool = False
    emergency_brake: bool = False
    manual_mode: bool = False
    interior_temperature_control: int = 70
    inside_lights: bool = False
    outside_lights: bool = False
    right_side_doors: bool = False
    left_side_doors: bool = False
    activate_announcement: bool = False
