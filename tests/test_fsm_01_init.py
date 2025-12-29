# tests/test_fsm_01_init.py

import pytest
from object_editor.fsm.context import FSMContext
from object_editor.fsm.events import Event
from object_editor.fsm.scene_managers import IdleSceneManager, AddIdleSceneManager

def test_fsm_initial_state_idle():
    """FSM должен инициализироваться в состоянии Idle"""
    fsm = FSMContext(IdleSceneManager)  # передаем класс состояния

    # Проверяем, что начальное состояние Idle
    assert isinstance(fsm.state, IdleSceneManager)

    # При включении кнопки Add FSM должен перейти в AddIdle (тип объекта еще не выбран)
    fsm.dispatch(Event.ADD_BUTTON_ON)
    assert isinstance(fsm.state, AddIdleSceneManager)
