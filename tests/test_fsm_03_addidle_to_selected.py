# tests/test_fsm_03_addidle_to_selected.py

from object_editor.fsm.context import FSMContext
from object_editor.fsm.events import Event
from object_editor.fsm.scene_managers import IdleSceneManager, AddIdleSceneManager, SelectedSceneManager


def test_addidle_to_selected_on_left_press_object():
    """AddIdleSceneManager + LEFT_PRESS_OBJECT → SelectedSceneManager (тип предмета не выбран)"""
    fsm = FSMContext(IdleSceneManager)

    # Сначала нажимаем кнопку ADD → AddIdleSceneManager
    fsm.dispatch(Event.ADD_BUTTON_ON)
    assert isinstance(fsm.state, AddIdleSceneManager)

    # Клик по объекту
    fsm.dispatch(Event.LEFT_PRESS_OBJECT)

    # Проверяем переход
    assert isinstance(fsm.state, SelectedSceneManager)
