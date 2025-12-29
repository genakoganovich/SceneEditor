# tests/test_fsm_09_idle_stable.py

from object_editor.fsm.context import FSMContext
from object_editor.fsm.events import Event
from object_editor.fsm.scene_managers import IdleSceneManager


def test_idle_stable_events():
    """IdleSceneManager + события, которые не должны менять состояние → остаёмся в IdleSceneManager"""
    fsm = FSMContext(IdleSceneManager)

    # Проверяем начальное состояние
    assert isinstance(fsm.state, IdleSceneManager)

    # Список событий, которые не должны менять состояние
    events = [
        Event.LEFT_PRESS_EMPTY,
        Event.RIGHT_PRESS_OBJECT,
        Event.RIGHT_PRESS_EMPTY,
        Event.ADD_BUTTON_OFF,
        Event.SELECT_OBJECT_TYPE
    ]

    for event in events:
        fsm.dispatch(event)
        assert isinstance(fsm.state, IdleSceneManager)
