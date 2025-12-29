# tests/test_fsm_10_addidle_to_idle.py

from object_editor.fsm.context import FSMContext
from object_editor.fsm.events import Event
from object_editor.fsm.scene_managers import AddIdleSceneManager, IdleSceneManager


def test_addidle_to_idle_on_add_button_off():
    """AddIdleSceneManager + ADD_BUTTON_OFF → IdleSceneManager"""
    fsm = FSMContext(AddIdleSceneManager)

    # Проверяем начальное состояние
    assert isinstance(fsm.state, AddIdleSceneManager)

    # Отправляем событие ADD_BUTTON_OFF
    fsm.dispatch(Event.ADD_BUTTON_OFF)

    # Проверяем, что FSM перешёл в Idle
    assert isinstance(fsm.state, IdleSceneManager)
