# tests/test_fsm_04_addidle_left_press_empty.py

from object_editor.fsm.context import FSMContext
from object_editor.fsm.events import Event
from object_editor.fsm.scene_managers import IdleSceneManager, AddIdleSceneManager


def test_addidle_left_press_empty_no_object_type():
    """AddIdleSceneManager + LEFT_PRESS_EMPTY → AddIdleSceneManager (тип предмета не выбран)"""
    fsm = FSMContext(IdleSceneManager)

    # Нажимаем кнопку ADD → AddIdleSceneManager
    fsm.dispatch(Event.ADD_BUTTON_ON)
    assert isinstance(fsm.state, AddIdleSceneManager)

    # Левый клик по пустому месту
    fsm.dispatch(Event.LEFT_PRESS_EMPTY)

    # Проверяем, что состояние не изменилось
    assert isinstance(fsm.state, AddIdleSceneManager)
