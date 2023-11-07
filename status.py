from enum import Enum


class Status(Enum):
    IDLE = 1
    IN_TRANSIT = 2
    DROPPING_OFF = 3
    PICKING_UP = 4
