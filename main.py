from object_editor.fsm.context import FSMContext
from object_editor.fsm.events import Event
from object_editor.fsm.scene_managers import IdleSceneManager

if __name__ == "__main__":
    # Создаём FSM с начальным состоянием IdleSceneManager
    fsm_ctx = FSMContext(IdleSceneManager)

    # Пример событий
    fsm_ctx.dispatch(Event.ADD_BUTTON_ON)
    fsm_ctx.dispatch(Event.LEFT_PRESS_OBJECT)
    fsm_ctx.dispatch(Event.RIGHT_PRESS_OBJECT)
    fsm_ctx.dispatch(Event.ADD_BUTTON_OFF)
