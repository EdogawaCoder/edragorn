from enum import Enum


class BrainState(Enum):
        idle = "IDLE"
        searching = "SEARCHING"
        target_found = "TARGET_FOUND"
        tracking = "TRACKING"