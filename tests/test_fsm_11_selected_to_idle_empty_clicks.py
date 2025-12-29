# tests/test_fsm_11_selected_to_idle_empty_clicks.py

from object_editor.fsm.context import FSMContext
from object_editor.fsm.events import Event
from object_editor.fsm.scene_managers import SelectedSceneManager, IdleSceneManager


def test_selected_to_idle_on_empty_clicks():
    """SelectedSceneManager + LEFT_PRESS_EMPTY / RIGHT_PRESS_EMPTY → IdleSceneManager"""
    fsm = FSMContext(SelectedSceneManager)

    # Проверяем начальное состояние
    assert isinstance(fsm.state, SelectedSceneManager)

    # Левый клик на пустое место
    fsm.dispatch(Event.LEFT_PRESS_EMPTY)
    assert isinstance(fsm.state, IdleSceneManager)

    # Сброс FSM обратно в Selected для проверки правого клика
    fsm = FSMContext(SelectedSceneManager)

    # Правый клик на пустое место
    fsm.dispatch(Event.RIGHT_PRESS_EMPTY)
    assert isinstance(fsm.state, IdleSceneManager)
