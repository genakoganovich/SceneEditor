# tests/test_fsm_02_addidle_to_selected.py

import pytest
from object_editor.fsm.context import FSMContext
from object_editor.fsm.events import Event
from object_editor.fsm.scene_managers import IdleSceneManager, AddIdleSceneManager, SelectedSceneManager

def test_addidle_left_press_object_to_selected():
    """AddIdle + LEFT_PRESS_OBJECT → Selected (выбор объекта, тип не выбран)"""
    fsm = FSMContext(IdleSceneManager)

    # Переход в AddIdle через нажатие кнопки Add
    fsm.dispatch(Event.ADD_BUTTON_ON)
    assert isinstance(fsm.state, AddIdleSceneManager)

    # Левый клик по объекту → переход в Selected
    fsm.dispatch(Event.LEFT_PRESS_OBJECT)
    assert isinstance(fsm.state, SelectedSceneManager)
