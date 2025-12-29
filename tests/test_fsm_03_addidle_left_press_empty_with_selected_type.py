# tests/test_fsm_03_addidle_left_press_empty_with_selected_type.py

import pytest
from object_editor.fsm.context import FSMContext
from object_editor.fsm.events import Event
from object_editor.fsm.scene_managers import IdleSceneManager, AddIdleSceneManager, AddSceneManager

def test_addidle_left_press_empty_with_selected_type():
    """AddIdle + LEFT_PRESS_EMPTY с выбранным типом → AddSceneManager (добавление объекта)"""
    fsm = FSMContext(IdleSceneManager)

    # Нажимаем Add → AddIdle
    fsm.dispatch(Event.ADD_BUTTON_ON)
    assert isinstance(fsm.state, AddIdleSceneManager)

    # Выбираем тип объекта (симуляция SELECT_OBJECT_TYPE)
    fsm.dispatch(Event.SELECT_OBJECT_TYPE)
    # Переход в AddSceneManager
    fsm.dispatch(Event.LEFT_PRESS_EMPTY)
    assert isinstance(fsm.state, AddSceneManager)
