from dataclasses import dataclass


@dataclass
class TrainModelInput:
    command_set_point: float = 0.0
    authority: bool = False
    current_set_point: float = 0.0
    brake_failure: bool = False
    signal_pickup_failure: bool = False
    engine_failure: bool = False
    station_name: str = "YARD"