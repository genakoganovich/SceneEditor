# tests/test_fsm_07_selected_to_idle.py

from object_editor.fsm.context import FSMContext
from object_editor.fsm.events import Event
from object_editor.fsm.scene_managers import IdleSceneManager, AddIdleSceneManager, AddSceneManager, SelectedSceneManager


def test_selected_to_idle_on_right_press_or_left_release():
    """SelectedSceneManager + RIGHT_PRESS_OBJECT / LEFT_RELEASE → IdleSceneManager"""
    fsm = FSMContext(IdleSceneManager)

    # Переходим в SelectedSceneManager
    fsm.dispatch(Event.ADD_BUTTON_ON)          # Idle → AddIdle
    fsm.dispatch(Event.LEFT_PRESS_OBJECT)      # AddIdle → Selected
    assert isinstance(fsm.state, SelectedSceneManager)

    # Тест RIGHT_PRESS_OBJECT
    fsm.dispatch(Event.RIGHT_PRESS_OBJECT)
    assert isinstance(fsm.state, IdleSceneManager)

    # Снова в SelectedSceneManager
    fsm.dispatch(Event.ADD_BUTTON_ON)          # Idle → AddIdle
    fsm.dispatch(Event.LEFT_PRESS_OBJECT)      # AddIdle → Selected
    assert isinstance(fsm.state, SelectedSceneManager)

    # Тест LEFT_RELEASE
    fsm.dispatch(Event.LEFT_RELEASE)
    assert isinstance(fsm.state, IdleSceneManager)
