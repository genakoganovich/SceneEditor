# object_editor/fsm/actions.py

from enum import Enum, auto

class Action(Enum):
    PICK_OBJECT = auto()
    HIGHLIGHT_OBJECT = auto()
    CLEAR_SELECTION = auto()
    DELETE_OBJECT = auto()
    MOVE_OBJECT = auto()
