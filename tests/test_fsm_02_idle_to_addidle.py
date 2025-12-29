# tests/test_fsm_02_idle_to_addidle.py

from object_editor.fsm.context import FSMContext
from object_editor.fsm.events import Event
from object_editor.fsm.scene_managers import IdleSceneManager, AddIdleSceneManager


def test_idle_to_addidle_on_add_button_on():
    """Idle + ADD_BUTTON_ON → AddIdleSceneManager (тип предмета не выбран)"""
    fsm = FSMContext(IdleSceneManager)

    # Нажатие кнопки ADD
    fsm.dispatch(Event.ADD_BUTTON_ON)

    # Проверяем переход
    assert isinstance(fsm.state, AddIdleSceneManager)
