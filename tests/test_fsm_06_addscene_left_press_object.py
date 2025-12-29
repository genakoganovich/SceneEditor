# tests/test_fsm_06_addscene_left_press_object.py

from object_editor.fsm.context import FSMContext
from object_editor.fsm.events import Event
from object_editor.fsm.scene_managers import IdleSceneManager, AddIdleSceneManager, AddSceneManager, SelectedSceneManager


def test_addscene_left_press_object_selected():
    """AddSceneManager + LEFT_PRESS_OBJECT (тип выбран) → SelectedSceneManager"""
    fsm = FSMContext(IdleSceneManager)

    # Нажимаем кнопку ADD → AddIdleSceneManager
    fsm.dispatch(Event.ADD_BUTTON_ON)
    assert isinstance(fsm.state, AddIdleSceneManager)

    # Выбираем тип объекта → AddSceneManager
    fsm.dispatch(Event.SELECT_OBJECT_TYPE)
    assert isinstance(fsm.state, AddSceneManager)

    # Левый клик по объекту → SelectedSceneManager
    fsm.dispatch(Event.LEFT_PRESS_OBJECT)
    assert isinstance(fsm.state, SelectedSceneManager)
