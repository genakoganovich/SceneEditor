# tests/test_fsm_08_selected_to_selected.py

from object_editor.fsm.context import FSMContext
from object_editor.fsm.events import Event
from object_editor.fsm.scene_managers import IdleSceneManager, SelectedSceneManager


def test_selected_to_selected_on_left_press_object():
    """SelectedSceneManager + LEFT_PRESS_OBJECT на другом объекте → остаёмся в SelectedSceneManager"""
    fsm = FSMContext(IdleSceneManager)

    # Переходим в SelectedSceneManager
    fsm.dispatch(Event.ADD_BUTTON_ON)          # Idle → AddIdle
    fsm.dispatch(Event.LEFT_PRESS_OBJECT)      # AddIdle → Selected
    assert isinstance(fsm.state, SelectedSceneManager)

    # Кликаем по другому объекту
    fsm.dispatch(Event.LEFT_PRESS_OBJECT)
    # Состояние должно остаться SelectedSceneManager
    assert isinstance(fsm.state, SelectedSceneManager)
