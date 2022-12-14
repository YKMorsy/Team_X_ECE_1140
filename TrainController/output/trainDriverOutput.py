from dataclasses import dataclass


@dataclass
class TrainDriverOutput:
    current_set_point: float = 0.0
    speed_limit: float = 0.0
    interior_temperature: int = 70
    command_set_point: float = 0.0
    brake_failure: bool = False
    engine_failure: bool = False
    wheel_failure: bool = False
    signal_pickup_failure: bool = False
    authority: bool = False
    next_stop: str = ""
    train_movement: bool = False
    power: float = 0.0