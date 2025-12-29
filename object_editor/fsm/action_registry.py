from .actions import Action
from .events import Event
from .scene_managers import (
    IdleSceneManager,
    AddIdleSceneManager,
    AddSceneManager,
    SelectedSceneManager,
)

# -------- PRE actions --------
PRE_ACTIONS = {
    (IdleSceneManager, Event.LEFT_PRESS_OBJECT): [Action.PICK_OBJECT],
    (AddIdleSceneManager, Event.LEFT_PRESS_OBJECT): [Action.PICK_OBJECT],
    (AddSceneManager, Event.LEFT_PRESS_OBJECT): [Action.PICK_OBJECT],
    (SelectedSceneManager, Event.LEFT_PRESS_OBJECT): [Action.PICK_OBJECT],
}

# -------- POST actions --------
POST_ACTIONS = {
    (SelectedSceneManager, Event.LEFT_PRESS_OBJECT): [Action.HIGHLIGHT_OBJECT],

    (SelectedSceneManager, Event.RIGHT_PRESS_OBJECT): [
        Action.DELETE_OBJECT,
        Action.CLEAR_SELECTION,
    ],

    (SelectedSceneManager, Event.LEFT_RELEASE): [
        Action.MOVE_OBJECT,
        Action.CLEAR_SELECTION,
    ],
}
