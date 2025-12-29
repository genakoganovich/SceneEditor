# object_editor/fsm/action_registry.py

from object_editor.fsm.actions import Action
from object_editor.fsm.events import Event
from object_editor.fsm.scene_managers import (
    IdleSceneManager,
    AddIdleSceneManager,
    AddSceneManager,
    SelectedSceneManager,
)

# Ключ: (StateClass, Event)
# Значение: список Action
ACTION_REGISTRY = {
    # ---------------- AddIdle ----------------
    (AddIdleSceneManager, Event.LEFT_PRESS_OBJECT): [
        Action.HIGHLIGHT_OBJECT
    ],

    # ---------------- AddScene ----------------
    (AddSceneManager, Event.LEFT_PRESS_EMPTY): [
        Action.ADD_OBJECT,
        Action.CLEAR_SELECTION,
    ],

    # ---------------- Selected ----------------
    (SelectedSceneManager, Event.RIGHT_PRESS_OBJECT): [
        Action.DELETE_OBJECT,
        Action.CLEAR_SELECTION,
    ],
    (SelectedSceneManager, Event.LEFT_RELEASE): [
        Action.MOVE_OBJECT,
        Action.CLEAR_SELECTION,
    ],
    (SelectedSceneManager, Event.LEFT_PRESS_OBJECT): [
        Action.HIGHLIGHT_OBJECT,
    ],
    (SelectedSceneManager, Event.LEFT_PRESS_EMPTY): [
        Action.CLEAR_SELECTION,
    ],
}
