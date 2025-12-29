# object_editor/fsm/actions.py

from enum import Enum, auto


class Action(Enum):
    ADD_OBJECT = auto()
    DELETE_OBJECT = auto()
    MOVE_OBJECT = auto()
    HIGHLIGHT_OBJECT = auto()
    CLEAR_SELECTION = auto()
