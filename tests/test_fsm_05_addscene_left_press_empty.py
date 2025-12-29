# tests/test_fsm_05_addscene_left_press_empty.py

from object_editor.fsm.context import FSMContext
from object_editor.fsm.events import Event
from object_editor.fsm.scene_managers import IdleSceneManager, AddIdleSceneManager, AddSceneManager


def test_addscene_left_press_empty_addidle():
    """AddSceneManager + LEFT_PRESS_EMPTY → AddIdleSceneManager (тип выбран)"""
    fsm = FSMContext(IdleSceneManager)

    # Нажимаем кнопку ADD → AddIdleSceneManager
    fsm.dispatch(Event.ADD_BUTTON_ON)
    assert isinstance(fsm.state, AddIdleSceneManager)

    # Выбираем тип объекта → AddSceneManager
    fsm.dispatch(Event.SELECT_OBJECT_TYPE)
    assert isinstance(fsm.state, AddSceneManager)

    # Левый клик по пустому месту → AddIdleSceneManager
    fsm.dispatch(Event.LEFT_PRESS_EMPTY)
    assert isinstance(fsm.state, AddIdleSceneManager)
