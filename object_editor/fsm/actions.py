# object_editor/fsm/actions.py

from enum import Enum, auto

class Action(Enum):
    PICK_OBJECT = auto()
    HIGHLIGHT_OBJECT = auto()
    CLEAR_SELECTION = auto()
    DELETE_OBJECT = auto()
    MOVE_OBJECT = auto()
    ADD_BUTTON_ON = auto()
    ADD_BUTTON_OFF = auto()
    LEFT_PRESS_OBJECT = auto()
    RIGHT_PRESS_OBJECT = auto()
    LEFT_RELEASE = auto()
